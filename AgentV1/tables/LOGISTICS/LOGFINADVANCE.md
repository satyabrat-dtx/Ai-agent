# DB2ADMIN.LOGFINADVANCE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 37
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201897

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `ADVANCENUMBER` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `ADVANCETYPE` | CHAR(5) |  |  |  |  |
| 4 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `FINANCIALYEAR` | CHAR(4) |  |  |  |  |
| 6 | `REFERENCENOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `REFERENCENOCODE` | CHAR(15) |  |  |  |  |
| 8 | `POSTINGDATE` | DATE |  |  |  |  |
| 9 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 11 | `SUBLEDGERCODE` | CHAR(8) |  |  |  |  |
| 12 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 13 | `BANKREFDATE` | DATE |  |  |  |  |
| 14 | `VALUEDATE` | DATE |  |  |  |  |
| 15 | `BANKCHARGESINR` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ADVANCEAMOUNTUSD` | DECIMAL(18,5) |  |  |  |  |
| 17 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 18 | `OTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 19 | `PROFITCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `PROFITCENTERCODE` | CHAR(20) |  |  |  |  |
| 21 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 23 | `FINADVANCELOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 32 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 33 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 34 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 35 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 36 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINADVANCE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.ADVANCENUMBER,
       t.ADVANCETYPE,
       t.DOCUMENTTYPECODE,
       t.FINANCIALYEAR,
       t.REFERENCENOCOUNTERCODE,
       t.REFERENCENOCODE,
       t.POSTINGDATE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.SUBLEDGERCODE
FROM   DB2ADMIN.LOGFINADVANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
