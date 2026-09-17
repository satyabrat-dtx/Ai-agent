# DB2ADMIN.PRODUCTIONPROGRESSIMPORT

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 85
- **Primary key**: `COMPANYCODE`, `PROGRESSNUMBERPREFIX`, `PROGRESSNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 68398

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `NOWPROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 3 | `PROGRESSNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `EXTERNALPROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 5 | `PROGRESSLOADDATE` | DATE | NOT NULL |  |  |  |
| 6 | `PROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `PARTIALSTEP` | SMALLINT | NOT NULL |  |  |  |
| 8 | `OPERATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 10 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 11 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 13 | `ELEMENTITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 14 | `ELEMENTELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 15 | `ELEMENTELEMENTCODE` | CHAR(15) |  |  |  |  |
| 16 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 17 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 18 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 19 | `DATASETCODE` | CHAR(20) |  |  |  |  |
| 20 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 21 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 22 | `PROGRESSTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 23 | `PROGRESSSTARTQUEUEDATE` | DATE |  |  |  |  |
| 24 | `PROGRESSSTARTQUEUETIME` | TIME |  |  |  |  |
| 25 | `PROGRESSSTARTPREPROCESSDATE` | DATE |  |  |  |  |
| 26 | `PROGRESSSTARTPREPROCESSTIME` | TIME |  |  |  |  |
| 27 | `PROGRESSSTARTPROCESSDATE` | DATE |  |  |  |  |
| 28 | `PROGRESSSTARTPROCESSTIME` | TIME |  |  |  |  |
| 29 | `PROGRESSSTARTPOSTPROCESSDATE` | DATE |  |  |  |  |
| 30 | `PROGRESSSTARTPOSTPROCESSTIME` | TIME |  |  |  |  |
| 31 | `PROGRESSPARTIALENDDATE` | DATE |  |  |  |  |
| 32 | `PROGRESSPARTIALENDTIME` | TIME |  |  |  |  |
| 33 | `PROGRESSENDDATE` | DATE |  |  |  |  |
| 34 | `PROGRESSENDTIME` | TIME |  |  |  |  |
| 35 | `CALSHIFTDAILYINFORMATION` | INTEGER | NOT NULL |  |  |  |
| 36 | `QUEUEPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 37 | `PREPROCESSPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 38 | `PROCESSPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `POSTPROCESSPORTIONCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 40 | `QUEUERECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 41 | `PREPROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 42 | `PROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 43 | `POSTPROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 44 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 46 | `COSTELEMENTUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `QUEUERCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 48 | `PREPROCESSRCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 49 | `PROCESSRCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 50 | `POSTPROCESSRCORDEDCOSTELEMENTS` | DECIMAL(15,5) |  |  |  |  |
| 51 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 52 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 54 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `PACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `QUALITYITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 59 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 60 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 61 | `MACHINECODE` | CHAR(8) |  |  |  |  |
| 62 | `OPERATORCODE` | CHAR(8) |  |  |  |  |
| 63 | `DYELOTWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 64 | `DYELOTWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 65 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 66 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 67 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 68 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 69 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 70 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 71 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 72 | `DELETEPROGRESSPROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 73 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 74 | `PROGRESSNUMBERPREFIX` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 75 | `GROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 76 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 77 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 78 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 79 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 80 | `PROGRESSTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `MACHINEDOWNTIMETYPE` | CHAR(1) |  |  |  |  |
| 82 | `OPERATOR2CODE` | CHAR(8) |  |  |  |  |
| 83 | `OPERATOR3CODE` | CHAR(8) |  |  |  |  |
| 84 | `COMMENTARY` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODPROGIMP01` (IMPORTSTATUS, COMPANYCODE, PROGRESSNUMBER)
- `PRODUCTIONPROGRESSIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTSTATUS,
       t.COMPANYCODE,
       t.NOWPROGRESSNUMBER,
       t.PROGRESSNUMBER,
       t.EXTERNALPROGRESSNUMBER,
       t.PROGRESSLOADDATE,
       t.PROGRESSTEMPLATECODE,
       t.PARTIALSTEP,
       t.OPERATIONTYPE,
       t.PRODUCTIONORDERCODE,
       t.GROUPSTEPNUMBER,
       t.DEMANDCOUNTERCODE
FROM   DB2ADMIN.PRODUCTIONPROGRESSIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
