from django.shortcuts import render
# Author gt401
from .models import Jobcard, Operation, Realisedby, Workstation, Order, Job, Uses
from .classes import JobCardResponse, OperationResponse, OperationAtWorkstationResponse, JobsResponse
from .forms import StartStopForm
from django.views.decorators.cache import cache_control
import qrcode
import base64
from PIL import Image
from io import BytesIO
from datetime import datetime

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def list_of_orders(request):
    orders = Order.objects.all()
    template = 'adminsys/jobcard/list_of_orders.html'
    context = {'orders':orders}
    return render(request, template, context)        


def list_of_jobs(request, oid):
    order = list(Order.objects.filter(orderid=oid))[0]
    jobs = JobsResponse.JobsResponse(Job.objects.filter(orderid=oid))
    print(len(jobs.jobModels))
    for j in jobs.jobModels:
        jobcards = Jobcard.objects.filter(jobid=j.jobid)
        jobs.addJobCard(jobcards)
    jobs.setOrder(order)
    template = 'adminsys/jobcard/list_of_jobs.html'
    context = {'jobs':jobs}
    return render(request, template, context)        

def create_test_image():
        file = BytesIO()
        image = qrcode.make('123456')#Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save('qr.png')
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

def jobcard(request, jcid):
    jobcard = Jobcard.objects.filter(jobcardid=jcid)
    for jc in jobcard:
        jcr = JobCardResponse.JobCardResponse(jc)
        operations = Operation.objects.filter(jobcardid=jc.jobcardid)
        for op in operations:
            opr = OperationResponse.OperationResponse(op)
            realisedbys = Realisedby.objects.filter(operationid=op.operationid)
            for rb in realisedbys:
                opr.setWorkstation(rb.wsid)
            jcr.addOperation(opr)
        uses = Uses.objects.filter(jobcardid=jc.jobcardid)
        for use in uses:
            jcr.addUse(use)
    img = qrcode.make(jcr.jobModel.barcode)
    file = BytesIO()
    img.save(file, 'png')
    jcr.setQRCode(base64.b64encode(file.getvalue()).decode())   
    template = 'adminsys/jobcard/jobcard.html'
    context = {'jobcardr':jcr}
    return render(request, template, context)

def operation_at_workstation(request, opid, wid, jcid):
    print("here")
    print("here here")
    ops = list(Operation.objects.filter(jobcardid=jcid, operationid=opid))
    op = ops[0]
    rbs = list(Realisedby.objects.filter(operationid=op.operationid, wsid=wid))
    wss = list(Workstation.objects.filter(wsid=wid))
    oawr = OperationAtWorkstationResponse.OperationAtWorkstationResponse(op, wss[0], rbs[0])
    oawr.setParams(opid, wid, jcid)
    template = 'adminsys/jobcard/operation_at_workstation.html'
    context = {'oawr':oawr}
    return render(request, template, context)

def start_operation(request):
    #if request.method == 'POST':
    opid = request.POST.get("opid")
    wid = request.POST.get("wid")
    jcid = request.POST.get("jcid")
    ops = list(Operation.objects.filter(jobcardid=jcid, operationid=opid))
    op = ops[0]
    rbs = list(Realisedby.objects.filter(operationid=op.operationid, wsid=wid))
    rbs[0].start = datetime.now()
    wss = list(Workstation.objects.filter(wsid=wid))
    oawr = OperationAtWorkstationResponse.OperationAtWorkstationResponse(op, wss[0], rbs[0])
    oawr.setParams(opid, wid, jcid)
    #else:
    #print("else")
    template = 'adminsys/jobcard/operation_at_workstation.html'
    context = {'oawr':oawr}
    return render(request, template, context)

def end_operation(request):
    #if request.method == 'POST':
    opid = request.POST.get("opid")
    wid = request.POST.get("wid")
    jcid = request.POST.get("jcid")
    start = request.POST.get("start")
    ops = list(Operation.objects.filter(jobcardid=jcid, operationid=opid))
    op = ops[0]
    rbs = list(Realisedby.objects.filter(operationid=op.operationid, wsid=wid))
    rbs[0].end = datetime.now()
    if start != "None":
        rbs[0].start = start
    wss = list(Workstation.objects.filter(wsid=wid))
    oawr = OperationAtWorkstationResponse.OperationAtWorkstationResponse(op, wss[0], rbs[0])
    oawr.setParams(opid, wid, jcid)
   #else:
    #print("else")
    template = 'adminsys/jobcard/operation_at_workstation.html'
    context = {'oawr':oawr}
    return render(request, template, context)

# Create your views here.
