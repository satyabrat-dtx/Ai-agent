# DB2ADMIN.LOGFINDOCUMENTLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 85
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 179970

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINDOCUMENTBUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `FINDOCUMENTFINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 3 | `FINDOCDOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 5 | `FINDOCUMENTCODE` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 7 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 10 | `GLCODE` | CHAR(20) |  |  |  |  |
| 11 | `CREDITLINE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 15 | `AMOUNTINDC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 16 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 17 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 18 | `AMOUNTINCC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 20 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 21 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 22 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 23 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 24 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 25 | `DESTINATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `ICFDLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `ICFDLBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 28 | `ICFDLFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 29 | `ICFDLDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `ICFDLSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 31 | `ICFDLCODE` | CHAR(15) |  |  |  |  |
| 32 | `REFERENCETEXT1` | CHAR(100) |  |  |  |  |
| 33 | `REFERENCETEXT2` | CHAR(50) |  |  |  |  |
| 34 | `REFERENCETEXT3` | CHAR(50) |  |  |  |  |
| 35 | `REFERENCETEXT4` | CHAR(50) |  |  |  |  |
| 36 | `REFERENCETEXT5` | CHAR(50) |  |  |  |  |
| 37 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 38 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 39 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 40 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 41 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 42 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 43 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 44 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 46 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 47 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 48 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 49 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 50 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 51 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 52 | `SIXTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 53 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 55 | `SEVENTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 56 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 57 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 58 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 59 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 60 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 61 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 62 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 63 | `RECONCILIATIONDATE` | DATE |  |  |  |  |
| 64 | `RECONCILEDBY` | CHAR(50) |  |  |  |  |
| 65 | `RECONCILETRANNO` | CHAR(15) |  |  |  |  |
| 66 | `RECONCILEDON` | TIMESTAMP |  |  |  |  |
| 67 | `ASSETNOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 68 | `ASSETNOCODE` | CHAR(15) |  |  |  |  |
| 69 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 70 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 71 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 72 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 73 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 74 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 75 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 76 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 77 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 78 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 79 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 80 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 81 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 82 | `DESTBUCODE` | CHAR(10) |  |  |  |  |
| 83 | `ICGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `ICGLCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGFINDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `LOGFINDOCUMENTLINE.FATHERID = LOGFINDOCUMENT.ABSUNIQUEID`
- child `LOGFINDOCUMENTLINETEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.FINDOCUMENTCOMPANYCODE,
       t.FINDOCUMENTBUSINESSUNITCODE,
       t.FINDOCUMENTFINANCIALYEARCODE,
       t.FINDOCDOCUMENTTEMPLATECODE,
       t.FINDOCSTATISTICALGROUPCODE,
       t.FINDOCUMENTCODE,
       t.ABSVERSIONNUMBER,
       t.LINENUMBER,
       t.LINETEMPLATECODE,
       t.COMPANYCODE,
       t.GLCODE,
       t.CREDITLINE
FROM   DB2ADMIN.LOGFINDOCUMENTLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
