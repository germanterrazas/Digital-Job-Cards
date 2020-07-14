class OperationResponse:
  workstation = None;
  operationModel = None;

  def __init__(self, operationModel):
    self.operationModel = operationModel

  def setWorkstation(self, workstation):
    self.workstation = workstation
