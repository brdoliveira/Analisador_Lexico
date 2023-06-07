-- Criação das tabelas na Azure

CREATE TABLE SensorData (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    SensorName NVARCHAR(50) NOT NULL,
    SensorValue FLOAT NOT NULL,
    CaptureDate DATETIME NOT NULL
);

CREATE TABLE CapturaGeoLoc (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Latitude FLOAT NOT NULL,
    Longitude FLOAT NOT NULL,
    CaptureDate DATETIME NOT NULL
);

CREATE TABLE WordClients (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Word NVARCHAR(50) NOT NULL,
    TypeWord NVARCHAR(50) NOT NULL,
    CaptureDate DATETIME NOT NULL
);

CREATE TABLE Feedbacks (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Phrase NVARCHAR(500) NOT NULL,
    TypeFeedback NVARCHAR(10) NOT NULL,
    CaptureDate DATETIME NOT NULL
);
