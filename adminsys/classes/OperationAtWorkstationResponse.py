class OperationAtWorkstationResponse:
  workstationModel = None;
  operationModel = None;
  realisedByModel = None;
  opid = None;
  wid = None;
  jcid = None;

  def __init__(self, operationModel, workstationModel, realisedByModel):
    self.operationModel = operationModel
    self.workstationModel = workstationModel
    self.realisedByModel = realisedByModel

  def setParams(self, opid, wid, jcid):
    self.opid = opid
    self.wid = wid
    self.jcid = jcid

