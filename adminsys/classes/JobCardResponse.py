class JobCardResponse:
  operations = []
  jobModel = None
  uses = []
  qrCode = None

  def __init__(self, jobModel):
    self.jobModel = jobModel
    self.operations = []
    self.uses = []
    self.qrCode = None

  def addOperation(self, operation):
    self.operations.append(operation)

  def addUse(self, use):
    self.uses.append(use)

  def setQRCode(self, qrCode):
    self.qrCode = qrCode
