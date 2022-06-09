import os
import uuid
import random
import starkbank
from flask import Flask, jsonify, request, Response
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

private_key_content = os.environ['PRIVATE_KEY']

# for project users:
project = starkbank.Project(
    environment="sandbox",
    id="6316094184751104",            
    private_key=private_key_content
)
starkbank.user = project  

def add_invoice():
    invoices = [starkbank.Invoice(
            amount=random.randint(1000, 3000),  
            name="Buzz Aldrin",
            tax_id="012.345.678-90"
        ) for x in range(random.randint(8, 12))]

    return starkbank.invoice.create(invoices)


def schedule_time():
    schedule_manager = BackgroundScheduler()
    schedule_manager.remove_all_jobs()
    schedule_manager.add_job(add_invoice, "interval", hours=3)
    schedule_manager.start()


@app.route('/webhook/invoice', methods=['POST'])
def transfer():    
    event = starkbank.event.parse(
        content=request.data.decode("utf-8"),
        signature=request.headers["Digital-Signature"],
    )

    if event.subscription == "invoice" and event.log.type == "credited":
        transfers = starkbank.transfer.create([
            starkbank.Transfer(
                amount=event.log.invoice.amount,
                tax_id="20.018.183/0001-80",
                name="Stark Bank S.A.",
                bank_code="20018183",
                branch_code="0001",
                account_number="6341320293482496",
                external_id=str(uuid.uuid4()),                    
            )
        ])
        print (transfers)
    return Response(status=200)


@app.route('/', methods=['GET'])
def index():
    return "ok"


if __name__ == "__main__":
    add_invoice()
    schedule_time()
    app.run(debug=True)