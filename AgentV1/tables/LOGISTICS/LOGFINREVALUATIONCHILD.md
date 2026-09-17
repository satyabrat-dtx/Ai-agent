# DB2ADMIN.LOGFINREVALUATIONCHILD

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 70
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229582

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINREVALUATIONCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINREVALUATIONBUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `FINREVALUATIONFNCYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 3 | `FINREVALUATIONREVALUATIONDATE` | DATE | NOT NULL |  |  |  |
| 4 | `FINREVALUATIONPROCESSTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `DETAILLINENO` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 6 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 7 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 10 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 14 | `DOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 15 | `DOCUMENTLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 16 | `CREDITLINE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 18 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 19 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `GLCODE` | CHAR(20) |  |  |  |  |
| 21 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 22 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 23 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 24 | `CLEAREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 25 | `OUTSTANDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 26 | `AMTINCC` | DECIMAL(18,5) |  |  |  |  |
| 27 | `AMTINDC` | DECIMAL(18,5) |  |  |  |  |
| 28 | `BALANCEINDC` | DECIMAL(18,5) |  |  |  |  |
| 29 | `BALANCEINCC` | DECIMAL(18,5) |  |  |  |  |
| 30 | `TRANSLATIONEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 31 | `ASONCURRENCYRATE` | DECIMAL(28,15) |  |  |  |  |
| 32 | `REVALUATIONGAINAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 33 | `REVALUATIONLOSSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 34 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 35 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 36 | `FIRSTUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 39 | `SNDUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 42 | `THIRDUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 45 | `FRUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 46 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 47 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 48 | `FIFTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 49 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 51 | `SIXTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 54 | `SEUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 55 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 57 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 58 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 59 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 60 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 61 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 62 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 63 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 64 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 65 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 66 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 67 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 68 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 69 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINREVALUATION**.`ABSUNIQUEID` (medium confidence — name = 'LOGFINREVALUATION' + recurring fragment 'CHILD' (seen in 6 tables))
  - JOIN predicate: `LOGFINREVALUATIONCHILD.FATHERID = LOGFINREVALUATION.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINREVALUATIONCOMPANYCODE,
       t.FINREVALUATIONBUSINESSUNITCODE,
       t.FINREVALUATIONFNCYEARCODE,
       t.FINREVALUATIONREVALUATIONDATE,
       t.FINREVALUATIONPROCESSTYPE,
       t.DETAILLINENO,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE
FROM   DB2ADMIN.LOGFINREVALUATIONCHILD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
