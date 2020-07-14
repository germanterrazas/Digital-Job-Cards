class JobsResponse:
  jobModels = [];
  jobCardModels = [];
  orderModel = None

  def __init__(self, jobModels):
    self.jobModels = jobModels
    self.jobCardModels = []
    self.jorderModel = None

  def addJobCard(self, jobCardModels):
  	self.jobCardModels.append(jobCardModels)

  def setOrder(self, order):
  	self.orderModel = order
