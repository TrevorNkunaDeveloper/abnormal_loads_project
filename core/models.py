from django.db import models

# Accounts Model
class Account(models.Model):
    dbAccountCode = models.CharField(max_length=20, primary_key=True)
    dbAcctType = models.CharField(max_length=20)
    dbAccount = models.CharField(max_length=100)
    dbBalance = models.DecimalField(max_digits=15, decimal_places=2)
    dbAccountStatus = models.CharField(max_length=1)
    dbEMail = models.CharField(max_length=100, blank=True, null=True)
    dbTelNo = models.CharField(max_length=20, blank=True, null=True)
    dbCelNo = models.CharField(max_length=20, blank=True, null=True)

# AccountType Model
class AccountType(models.Model):
    dbAcctType = models.CharField(max_length=1, primary_key=True)
    dbAcctDesc = models.CharField(max_length=50)

# Applications Model
class Application(models.Model):
    dbApplicationNo = models.IntegerField(primary_key=True)
    dbProvCode = models.CharField(max_length=10)
    dbOperatorCode = models.CharField(max_length=20)
    dbApplicationDate = models.DateTimeField()
    dbTransType = models.IntegerField()
    dbAccountCode = models.ForeignKey(Account, on_delete=models.CASCADE)
    dbOwnerCode = models.CharField(max_length=20)
    dbPermitType = models.IntegerField()
    dbOriginArea = models.CharField(max_length=100)
    dbDestination = models.CharField(max_length=100)
    dbLoadDesc = models.CharField(max_length=255)
    dbApplicationFee = models.DecimalField(max_digits=15, decimal_places=2)
    dbStatus = models.CharField(max_length=10)
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbInvoiceNo = models.IntegerField()

# Approval Model
class Approval(models.Model):
    dbKey = models.AutoField(primary_key=True)
    dbApplicationNo = models.ForeignKey(Application, on_delete=models.CASCADE)
    dbShc = models.BooleanField()
    dbChargeEngFee = models.BooleanField()
    dbCheckCond = models.CharField(max_length=255)
    dbReference = models.CharField(max_length=255)

# AV (Abnormal Vehicle) Model
class AV(models.Model):
    dbAVNo = models.CharField(max_length=20, primary_key=True)
    dbOwnerCode = models.CharField(max_length=20)
    dbVType = models.CharField(max_length=50)
    dbOTBaseWidth = models.DecimalField(max_digits=10, decimal_places=2)
    dbWTrack = models.DecimalField(max_digits=10, decimal_places=2)
    dbMass = models.DecimalField(max_digits=10, decimal_places=2)
    dbPayloadLimit = models.DecimalField(max_digits=10, decimal_places=2)
    dbPayloadFactor = models.DecimalField(max_digits=10, decimal_places=2)
    dbHtLimit = models.DecimalField(max_digits=10, decimal_places=2)
    dbSpeedLimit = models.DecimalField(max_digits=10, decimal_places=2)
    dbChkTruck = models.BooleanField()
    dbChkOffRoad = models.BooleanField()
    dbChkCond = models.BooleanField()
    dbChkSteer = models.BooleanField()
    dbBM_Ratio = models.DecimalField(max_digits=10, decimal_places=2)
    dbSF_Ratio = models.DecimalField(max_digits=10, decimal_places=2)

# AV_Axles Model
class AV_Axle(models.Model):
    dbAVNo = models.ForeignKey(AV, on_delete=models.CASCADE)
    dbVType = models.CharField(max_length=50)
    dbAxMass = models.DecimalField(max_digits=10, decimal_places=2)
    dbActMass = models.DecimalField(max_digits=10, decimal_places=2)
    dbNAxles = models.IntegerField()
    dbAxType = models.IntegerField()
    dbTyrePressure = models.DecimalField(max_digits=10, decimal_places=2)
    dbWheelSpacing = models.DecimalField(max_digits=10, decimal_places=2)
    dbUnladen = models.DecimalField(max_digits=10, decimal_places=2)
    dbMaxPayload = models.DecimalField(max_digits=10, decimal_places=2)
    dbEffWidth = models.DecimalField(max_digits=10, decimal_places=2)
    dbFirstToLast = models.DecimalField(max_digits=10, decimal_places=2)

# AV_BlockedRegNo Model
class AV_BlockedRegNo(models.Model):
    dbRegNo = models.CharField(max_length=20, primary_key=True)
    dbReason = models.CharField(max_length=255)

# AV_Dimensions Model
class AV_Dimension(models.Model):
    dbAVNo = models.ForeignKey(AV, on_delete=models.CASCADE)
    dbCode = models.CharField(max_length=10)
    dbValue = models.DecimalField(max_digits=10, decimal_places=2)

# Constants Model
class Constant(models.Model):
    dbFinYear = models.IntegerField()
    ID = models.AutoField(primary_key=True)
    dbProvCode = models.CharField(max_length=10)
    dbConstValue = models.DecimalField(max_digits=10, decimal_places=2)

# ConstantsDescription Model
class ConstantsDescription(models.Model):
    ID = models.AutoField(primary_key=True)
    dbConstName = models.CharField(max_length=50)
    dbConstDesc = models.CharField(max_length=255)

# Embargo Model
class Embargo(models.Model):
    dbFromDate = models.DateField()
    dbToDate = models.DateField()
    dbEmbDesc = models.CharField(max_length=255)

# EmbargoString Model
class EmbargoString(models.Model):
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbEmbargoDate = models.CharField(max_length=255)

# ePermits Model
class EPermit(models.Model):
    dbPermitNo = models.IntegerField(primary_key=True)
    dbAmendNo = models.IntegerField()
    dbProvCode = models.CharField(max_length=10)
    dbAccountCode = models.ForeignKey(Account, on_delete=models.CASCADE)
    dbPrinted = models.BooleanField()
    dbEMailed = models.BooleanField()
    ePermitGUID = models.CharField(max_length=50)

# Escorts Model
class Escort(models.Model):
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbFromKm = models.DecimalField(max_digits=10, decimal_places=2)
    dbToKm = models.DecimalField(max_digits=10, decimal_places=2)
    dbEscortType = models.CharField(max_length=50)
    dbNumEscorts = models.IntegerField()
    dbWeekend = models.BooleanField()
    dbSelfEscorts = models.IntegerField()

# Owners Model
class Owner(models.Model):
    dbOwnerCode = models.CharField(max_length=20, primary_key=True)
    dbOwner = models.CharField(max_length=100)
    dbOwnerAddr1 = models.CharField(max_length=255)
    dbOwnerAddr2 = models.CharField(max_length=255)
    dbOwnerAddr3 = models.CharField(max_length=255)
    dbTelNo = models.CharField(max_length=20)
    dbCelNo = models.CharField(max_length=20)
    dbOnHold = models.BooleanField()
    dbOnHoldReason = models.CharField(max_length=255)

# Route Model
class Route(models.Model):
    dbRouteCode = models.CharField(max_length=20, primary_key=True)
    dbRouteStart = models.CharField(max_length=100)
    dbRouteEnd = models.CharField(max_length=100)
    dbRouteDist = models.DecimalField(max_digits=10, decimal_places=2)
    dbHtLimit = models.DecimalField(max_digits=10, decimal_places=2)
    dbMassLimit = models.DecimalField(max_digits=10, decimal_places=2)
    dbWdthLimit = models.DecimalField(max_digits=10, decimal_places=2)

# RouteProvince Model
class RouteProvince(models.Model):
    dbRouteCode = models.ForeignKey(Route, on_delete=models.CASCADE)
    dbProvCode = models.CharField(max_length=10)
    dbPercentage = models.DecimalField(max_digits=5, decimal_places=2)

# InvoiceSequence Model
class InvoiceSequence(models.Model):
    dbInvoiceNo = models.IntegerField(primary_key=True)

# PBS_Permits Model
class PBSPermit(models.Model):
    dbPBS_No = models.IntegerField(primary_key=True)
    dbPermitsA = models.CharField(max_length=50)
    dbPermitsIssued = models.CharField(max_length=50)
    dbRegNos = models.CharField(max_length=50)

# PermitDist Model
class PermitDist(models.Model):
    RowPosition = models.IntegerField(primary_key=True)
    one_week = models.IntegerField()
    one_month = models.IntegerField()
    two_months = models.IntegerField()
    three_months = models.IntegerField()
    four_months = models.IntegerField()
    five_months = models.IntegerField()
    six_months = models.IntegerField()
    seven_months = models.IntegerField()
    eight_months = models.IntegerField()
    nine_months = models.IntegerField()
    ten_months = models.IntegerField()
    eleven_months = models.IntegerField()
    twelve_months = models.IntegerField()
    description = models.CharField(max_length=255)

# PermitProvince Model
class PermitProvince(models.Model):
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbProvCode = models.CharField(max_length=10)
    dbPercentage = models.DecimalField(max_digits=5, decimal_places=2)

# PermitSequence Model
class PermitSequence(models.Model):
    dbSequenceNo = models.IntegerField(primary_key=True)
    dbSequenceDate = models.DateField()

# Provinces Model
class Province(models.Model):
    dbProvIndex = models.IntegerField(primary_key=True)
    dbProvCode = models.CharField(max_length=10)
    dbProvince = models.CharField(max_length=100)
    dbAVRDownloadDate = models.DateField()

# RTIStn Model
class RTIStn(models.Model):
    dbRTIStn = models.CharField(max_length=50, primary_key=True)
    dbTelCode = models.CharField(max_length=20)
    dbRTITelNo = models.CharField(max_length=20)
    dbContact = models.CharField(max_length=100)

# StatusCodes Model
class StatusCode(models.Model):
    dbStatusCode = models.CharField(max_length=1, primary_key=True)
    dbStatusDescrip = models.CharField(max_length=255)

# Trans_QuotePermits Model
class TransQuotePermit(models.Model):
    dbQuoteNo = models.IntegerField()
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbCorrection = models.BooleanField()
    dbAmount = models.DecimalField(max_digits=15, decimal_places=2)

# Trans_Quotes Model
class TransQuote(models.Model):
    dbQuoteNo = models.IntegerField(primary_key=True)
    dbQuoteDate = models.DateTimeField()
    dbAccountCode = models.ForeignKey(Account, on_delete=models.CASCADE)

# Trans_RegNo Model
class TransRegNo(models.Model):
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbVType = models.CharField(max_length=50)
    dbRegNo = models.CharField(max_length=20)

# TransactionBook Model
class TransactionBook(models.Model):
    dbTransactionKey = models.AutoField(primary_key=True)
    dbTransactionDate = models.DateTimeField()
    dbTransactionType = models.CharField(max_length=10)
    dbPaymentMethod = models.CharField(max_length=10)
    dbAccountCode = models.ForeignKey(Account, on_delete=models.CASCADE)
    dbPermitNo = models.IntegerField()
    dbAmendNo = models.IntegerField()
    dbRemarks = models.CharField(max_length=255)
    dbReceiptNo = models.CharField(max_length=50)
    dbReceiptAmount = models.DecimalField(max_digits=15, decimal_places=2)
    dbReceiptDate = models.DateField()
    dbChequeNo = models.CharField(max_length=50)
    dbAmount = models.DecimalField(max_digits=15, decimal_places=2)
    dbBalance = models.DecimalField(max_digits=15, decimal_places=2)
    dbOwner = models.CharField(max_length=100)
    dbJobNo = models.CharField(max_length=50)
    dbInvoiceNo = models.IntegerField()

# Transaction Model
class Transaction(models.Model):
    dbPermitNo = models.IntegerField(primary_key=True)
    dbAmendNo = models.IntegerField(null=True, blank=True)
    dbFinYear = models.IntegerField()
    dbProvCode = models.CharField(max_length=10)
    dbCreateTime = models.DateTimeField()
    dbAcceptTime = models.DateTimeField(null=True, blank=True)
    dbIssueTime = models.DateTimeField(null=True, blank=True)
    dbTransactionKey = models.IntegerField()
    dbOperatorCode = models.CharField(max_length=20)
    dbEngineerCode = models.CharField(max_length=20, null=True, blank=True)
    dbAccountCode = models.CharField(max_length=20)
    dbAccountType = models.CharField(max_length=20)
    dbJobNo = models.CharField(max_length=50, null=True, blank=True)
    dbReferenceNo = models.CharField(max_length=50, null=True, blank=True)
    dbOwnerCode = models.CharField(max_length=20)
    dbOwner = models.CharField(max_length=100)
    dbOwnerAddr1 = models.CharField(max_length=255, null=True, blank=True)
    dbOwnerAddr2 = models.CharField(max_length=255, null=True, blank=True)
    dbOwnerAddr3 = models.CharField(max_length=255, null=True, blank=True)
    dbTelCode = models.CharField(max_length=10, null=True, blank=True)
    dbTelNo = models.CharField(max_length=20, null=True, blank=True)
    dbCelNo = models.CharField(max_length=20, null=True, blank=True)
    dbVehType = models.CharField(max_length=50)
    dbLaden = models.BooleanField(default=False)
    dbLdDesc = models.CharField(max_length=255, null=True, blank=True)
    dbLdLen = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dbLdWdth = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dbLdHt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.dbPermitNo} - {self.dbReferenceNo}"

 # Transaction Amended Model(Inherits from transaction)   
class TransactionsAmended(Transaction):
    class Meta:
        verbose_name = "Amended Transaction"
        verbose_name_plural = "Amended Transactions"
        db_table = "transactions_amended"

 # Transaction Cancelled Model(Inherits from transaction)   
class TransactionsCancelled(Transaction):
    class Meta:
        verbose_name = "Cancelled Transaction"
        verbose_name_plural = "Cancelled Transactions"
        db_table = "transactions_cancelled"

 # Transaction Corrected Model(Inherits from transaction)   
class TransactionsCorrected(Transaction):
    class Meta:
        verbose_name = "Corrected Transaction"
        verbose_name_plural = "Corrected Transactions"
        db_table = "transactions_corrected"



# User models
class User(models.Model):
    ROLE_CHOICES = [
        ('Supervisor', 'Supervisor'),
        ('Admin', 'Admin'),
        ('Operator', 'Operator'),
        ('Engineer','Engineer'),
        ('Auditor','Auditor')
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.full_name

