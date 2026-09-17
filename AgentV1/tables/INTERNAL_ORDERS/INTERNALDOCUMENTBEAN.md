# DB2ADMIN.INTERNALDOCUMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `staging_mirror`
- **Columns**: 126
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 66700

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PREVIOUSALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `CUSTOMERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 9 | `PROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `PROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 11 | `PROVISIONALDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `RESETDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DEFINITIVECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 15 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 16 | `GOODSISSUEDATE` | DATE |  |  |  |  |
| 17 | `ORDERDATE` | DATE |  |  |  |  |
| 18 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 19 | `ORDERPARTNERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 20 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 21 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 22 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 23 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 24 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 25 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 26 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 27 | `DELIVERYPOINTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 28 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 29 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 30 | `EXTERNALREFERENCECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 31 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 32 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 33 | `INTERNALREFERENCECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 34 | `DIVISIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 35 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 36 | `STATISTICALGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 37 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 38 | `COLLECTIONGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 40 | `PROJECTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 41 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 42 | `LANGUAGECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `DESTINATIONTYPE` | CHAR(1) |  |  |  |  |
| 44 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) |  |  |  |  |
| 45 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 46 | `DESTINATIONWAREHOUSECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 47 | `PREVIOUSDESTINATIONWHSCODE` | CHAR(8) |  |  |  |  |
| 48 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 49 | `TERMSOFDELIVERYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 51 | `TERMSOFSHIPPINGCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 52 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 53 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 54 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 55 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 56 | `AREACODE` | CHAR(3) |  |  |  |  |
| 57 | `AREACHANGED` | SMALLINT | NOT NULL |  |  |  |
| 58 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 59 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 60 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 61 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 62 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 63 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 64 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 65 | `WAREHOUSECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 66 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 67 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 68 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 69 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 70 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 71 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 72 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 73 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 74 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 75 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 76 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 77 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 78 | `STOCKTRANSACTIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 79 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 80 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 81 | `ORDERCATEGORYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 82 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 83 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 84 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 85 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 86 | `PROGRESSSTATUSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 87 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 88 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 89 | `PRINTEDDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 90 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 91 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 92 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 93 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 94 | `INTERNALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 95 | `INTERNALORDERCODE` | CHAR(15) |  |  |  |  |
| 96 | `ORDERPARTNERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 97 | `HIERARCHICQUERY` | SMALLINT | NOT NULL |  |  |  |
| 98 | `IMAGE` | CHAR(65) |  |  |  |  |
| 99 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 100 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 101 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 102 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 103 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 104 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 105 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 106 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 107 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 108 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 109 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 110 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 111 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 112 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 113 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 114 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 115 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 116 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 117 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 118 | `DESTPHYSWHSCODE` | CHAR(8) |  |  |  |  |
| 119 | `DESTZONECODE` | CHAR(3) |  |  |  |  |
| 120 | `DESTLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 121 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 122 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 123 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 124 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 125 | `ORGANIZER` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERNALDOCUMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.PREVIOUSALLOWEDDIVISIONS,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.CUSTOMERDESCRIPTION,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.PROVISIONALDOCUMENTDATE
FROM   DB2ADMIN.INTERNALDOCUMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
