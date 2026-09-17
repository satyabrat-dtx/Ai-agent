# DB2ADMIN.LOGFINACCAREACUSTOMIZEDOPT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 102143

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ACCOUNTAREA` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `DISCOUNTDEDUCTIONTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `MAXRATEDISCOUNT` | DECIMAL(7,2) |  |  |  |  |
| 5 | `BASEVALUE` | CHAR(1) |  |  |  |  |
| 6 | `TOLERANCEDAYSDOMESTIC` | INTEGER | NOT NULL |  |  |  |
| 7 | `TOLERANCEDAYSFOREIGN` | INTEGER | NOT NULL |  |  |  |
| 8 | `OTHERDEDUCTIONTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `MAXRATEOTHERDEDUCTIONS` | DECIMAL(7,2) |  |  |  |  |
| 10 | `GAINONEXCHANGECODE` | CHAR(5) |  |  |  |  |
| 11 | `LOSSONEXCHANGECODE` | CHAR(5) |  |  |  |  |
| 12 | `TOLERANCEDEBIT` | DECIMAL(7,2) |  |  |  |  |
| 13 | `TOLERANCEDEBITWITHDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 14 | `TOLERANCEDEBITDDNTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `TOLERANCECREDIT` | DECIMAL(7,2) |  |  |  |  |
| 16 | `TOLERANCECREDITWITHDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `TOLERANCECREDITDDNTYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `CLEARINGACTIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 25 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 26 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 27 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 28 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINACCAREACUSTOMIZEDOPT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ACCOUNTAREA,
       t.DISCOUNTDEDUCTIONTYPECODE,
       t.MAXRATEDISCOUNT,
       t.BASEVALUE,
       t.TOLERANCEDAYSDOMESTIC,
       t.TOLERANCEDAYSFOREIGN,
       t.OTHERDEDUCTIONTYPECODE,
       t.MAXRATEOTHERDEDUCTIONS,
       t.GAINONEXCHANGECODE,
       t.LOSSONEXCHANGECODE
FROM   DB2ADMIN.LOGFINACCAREACUSTOMIZEDOPT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
