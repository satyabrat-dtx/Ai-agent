# DB2ADMIN.PRODUCTIONPROGRESSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `staging_mirror`
- **Columns**: 106
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193754

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 3 | `EXTERNALPROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 4 | `PROGRESSLOADDATE` | DATE |  |  |  |  |
| 5 | `PROGRESSSTATUS` | CHAR(1) |  |  |  |  |
| 6 | `PROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `PARTIALSTEP` | SMALLINT | NOT NULL |  |  |  |
| 8 | `OPERATIONTYPE` | CHAR(1) |  |  |  |  |
| 9 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 10 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 11 | `GROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 12 | `PREVIOUSPROGRESSPROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 13 | `INACTIVE` | INTEGER | NOT NULL |  |  |  |
| 14 | `PROGRESSTYPE` | CHAR(1) |  |  |  |  |
| 15 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 16 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 17 | `ELEMENTITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 18 | `ELEMENTELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 19 | `ELEMENTELEMENTCODE` | CHAR(15) |  |  |  |  |
| 20 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 21 | `MANUALSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 22 | `EXTOPLINENOCHECK` | SMALLINT | NOT NULL |  |  |  |
| 23 | `EXTOPLINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 24 | `EXTOPLINECODE` | CHAR(15) |  |  |  |  |
| 25 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 26 | `SUPPLIERWAREHOUSETRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 27 | `EXTOPLINECANCEL` | SMALLINT | NOT NULL |  |  |  |
| 28 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 29 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 30 | `DATASETCODE` | CHAR(20) |  |  |  |  |
| 31 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 32 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 33 | `RELOADQUANTITYPERDEMANDGRID` | SMALLINT | NOT NULL |  |  |  |
| 34 | `PROGRESSSTARTQUEUEDATE` | DATE |  |  |  |  |
| 35 | `PROGRESSSTARTQUEUETIME` | TIME |  |  |  |  |
| 36 | `PROGRESSSTARTPREPROCESSDATE` | DATE |  |  |  |  |
| 37 | `PROGRESSSTARTPREPROCESSTIME` | TIME |  |  |  |  |
| 38 | `PROGRESSSTARTPROCESSDATE` | DATE |  |  |  |  |
| 39 | `PROGRESSSTARTPROCESSTIME` | TIME |  |  |  |  |
| 40 | `PROGRESSSTARTPOSTPROCESSDATE` | DATE |  |  |  |  |
| 41 | `PROGRESSSTARTPOSTPROCESSTIME` | TIME |  |  |  |  |
| 42 | `PROGRESSPARTIALENDDATE` | DATE |  |  |  |  |
| 43 | `PROGRESSPARTIALENDTIME` | TIME |  |  |  |  |
| 44 | `PROGRESSENDDATE` | DATE |  |  |  |  |
| 45 | `PROGRESSENDTIME` | TIME |  |  |  |  |
| 46 | `CALSHIFTDAILYINFORMATION` | INTEGER | NOT NULL |  |  |  |
| 47 | `QUEUEPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 48 | `PREPROCESSPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `PROCESSPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `POSTPROCESSPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 51 | `QUEUERECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 52 | `PREPROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 53 | `PROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 54 | `POSTPROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 55 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 57 | `COSTELEMENTUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `QUEUERCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 59 | `PREPROCESSRCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 60 | `PROCESSRCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 61 | `POSTPROCESSRCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 62 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `PACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 68 | `QUALITYITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 69 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 70 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 71 | `MACHINEDOWNTIMETYPE` | CHAR(1) |  |  |  |  |
| 72 | `MACHINECODE` | CHAR(8) |  |  |  |  |
| 73 | `OPERATORCODE` | CHAR(8) |  |  |  |  |
| 74 | `OPERATOR2CODE` | CHAR(8) |  |  |  |  |
| 75 | `OPERATOR3CODE` | CHAR(8) |  |  |  |  |
| 76 | `AUTOCALCULATEDQTY` | SMALLINT | NOT NULL |  |  |  |
| 77 | `AUTOCALCULATEDTIMES` | SMALLINT | NOT NULL |  |  |  |
| 78 | `DYELOTWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 79 | `DYELOTWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 80 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 81 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 82 | `DOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 83 | `COMMENTARY` | VARCHAR(250) |  |  |  |  |
| 84 | `EXTOPLINEENTITYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `EXTOPLINEENTITYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 86 | `EXTOPLINEENTITYCODE` | CHAR(15) |  |  |  |  |
| 87 | `EXTOPLINEENTITYORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 88 | `CALLSERVERSTATUS` | CHAR(1) |  |  |  |  |
| 89 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 90 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 91 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 92 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 93 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 94 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 95 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 96 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 97 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 98 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 99 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 100 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 101 | `CONNECTEXTOPDOC` | SMALLINT | NOT NULL |  |  |  |
| 102 | `EXTOPDOCUMENTPROVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 103 | `EXTOPDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 104 | `SELECTEDEXTOPDOC` | CHAR(90) |  |  |  |  |
| 105 | `MANUALPRODRESERVATIONLINKGRPCOD` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONPROGRESSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.PROGRESSNUMBER,
       t.EXTERNALPROGRESSNUMBER,
       t.PROGRESSLOADDATE,
       t.PROGRESSSTATUS,
       t.PROGRESSTEMPLATECODE,
       t.PARTIALSTEP,
       t.OPERATIONTYPE,
       t.PRODUCTIONORDERCODE,
       t.GROUPSTEPNUMBER,
       t.GROUPLINE
FROM   DB2ADMIN.PRODUCTIONPROGRESSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
