CREATE TABLE Group
(
  GroupID INT NOT NULL,
  Description VARCHAR(500) NOT NULL,
  Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (GroupID)
);

CREATE TABLE WorkStation
(
  WSID INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  Location VARCHAR(100) NOT NULL,
  PRIMARY KEY (WSID)
);

CREATE TABLE Material
(
  StockID INT NOT NULL,
  Description VARCHAR(500) NOT NULL,
  PRIMARY KEY (StockID)
);

CREATE TABLE Order
(
  OrderID INT NOT NULL,
  Description VARCHAR(500) NOT NULL,
  Date DATE NOT NULL,
  PRIMARY KEY (OrderID)
);

CREATE TABLE CAD
(
  FilePath VARCHAR(500) NOT NULL,
  CADID INT NOT NULL,
  PRIMARY KEY (CADID)
);

CREATE TABLE Inspection
(
  InspectionID INT NOT NULL,
  Comment VARCHAR(500) NOT NULL,
  Result INT NOT NULL,
  Date DATE NOT NULL,
  PRIMARY KEY (InspectionID)
);

CREATE TABLE User
(
  UserID INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  Description VARCHAR(500) NOT NULL,
  GroupID INT NOT NULL,
  PRIMARY KEY (UserID),
  FOREIGN KEY (GroupID) REFERENCES Group(GroupID)
);

CREATE TABLE Job
(
  JobID INT NOT NULL,
  Description VARCHAR(500) NOT NULL,
  CreationDate DATE NOT NULL,
  UserID INT NOT NULL,
  OrderID INT NOT NULL,
  CADID INT NOT NULL,
  PRIMARY KEY (JobID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
  FOREIGN KEY (CADID) REFERENCES CAD(CADID)
);

CREATE TABLE Uses
(
  Quantity FLOAT NOT NULL,
  JobID INT NOT NULL,
  StockID INT NOT NULL,
  PRIMARY KEY (JobID, StockID),
  FOREIGN KEY (JobID) REFERENCES Job(JobID),
  FOREIGN KEY (StockID) REFERENCES Material(StockID)
);

CREATE TABLE JobCard
(
  JobCardID INT NOT NULL,
  Description VARCHAR(500) NOT NULL,
  CreationDate DATE NOT NULL,
  UserID INT NOT NULL,
  JobID INT NOT NULL,
  PRIMARY KEY (JobCardID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (JobID) REFERENCES Job(JobID)
);

CREATE TABLE Operation
(
  OperationID INT NOT NULL,
  Description VARCHAR(500) NOT NULL,
  Number VARCHAR(100) NOT NULL,
  JobCardID INT NOT NULL,
  PRIMARY KEY (OperationID),
  FOREIGN KEY (JobCardID) REFERENCES JobCard(JobCardID)
);

CREATE TABLE RealisedBy
(
  Start DATE NOT NULL,
  End DATE NOT NULL,
  OperationID INT NOT NULL,
  WSID INT NOT NULL,
  PRIMARY KEY (OperationID, WSID),
  FOREIGN KEY (OperationID) REFERENCES Operation(OperationID),
  FOREIGN KEY (WSID) REFERENCES WorkStation(WSID)
);

CREATE TABLE InspectedBy
(
  InspectionID INT NOT NULL,
  OperationID INT NOT NULL,
  PRIMARY KEY (InspectionID, OperationID),
  FOREIGN KEY (InspectionID) REFERENCES Inspection(InspectionID),
  FOREIGN KEY (OperationID) REFERENCES Operation(OperationID)
);
