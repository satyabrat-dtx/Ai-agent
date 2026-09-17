# DB2ADMIN.LOGQUALITYDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 61
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208444

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DETAILREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 2 | `HEADERCODE` | CHAR(20) | NOT NULL |  |  |  |
| 3 | `HEADERSUBGROUPCODE` | CHAR(5) | NOT NULL |  |  |  |
| 4 | `HEADERNUMBERID` | INTEGER | NOT NULL |  |  |  |
| 5 | `HEADERLINE` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 6 | `HEADERDATE` | DATE | NOT NULL |  |  |  |
| 7 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 19 | `LOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 20 | `LOTCODE` | CHAR(35) | NOT NULL |  |  |  |
| 21 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) | NOT NULL |  |  |  |
| 23 | `ITEMELEMENTCODE` | CHAR(15) | NOT NULL |  |  |  |
| 24 | `DEMANDCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 25 | `DEMANDCODE` | CHAR(15) | NOT NULL |  |  |  |
| 26 | `PRODUCTIONORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 27 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 28 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 29 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 30 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 31 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 32 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 33 | `STATUS` | CHAR(2) | NOT NULL |  |  |  |
| 34 | `NOTEINTERNE` | VARCHAR(200) |  |  |  |  |
| 35 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 36 | `SAMPLEINSTRUCTIONCODE` | CHAR(3) |  |  |  |  |
| 37 | `SAMPLELENGTH` | DECIMAL(10,5) |  |  |  |  |
| 38 | `SAMPLENUMBER` | CHAR(50) |  |  |  |  |
| 39 | `TESTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 40 | `PROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 41 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 43 | `EXPORTEDTOPDM` | SMALLINT | NOT NULL |  |  |  |
| 44 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 45 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 46 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 47 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 48 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 49 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 50 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 51 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 52 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 53 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 54 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 55 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 56 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 57 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 58 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 59 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 60 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGQUALITYDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DETAILREQUIRED,
       t.HEADERCODE,
       t.HEADERSUBGROUPCODE,
       t.HEADERNUMBERID,
       t.HEADERLINE,
       t.HEADERDATE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.LOGQUALITYDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
