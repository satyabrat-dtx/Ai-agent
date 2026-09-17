# DB2ADMIN.LOGFINEXPNEGOTIATIONPC

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 21
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202936

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NEGOTIATIONCODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `BANKREFERENCENO` | CHAR(30) |  |  |  |  |
| 3 | `REFERENCEDATE` | DATE |  |  |  |  |
| 4 | `PACKINGCREDITLETTERNO` | CHAR(5) | NOT NULL |  |  |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `PACKINGCREDITVALUE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `PACKINGCREDITBALANCEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ADJUSTFORTHISBILL` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ADJUSTFCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 12 | `REMARKS` | CHAR(100) |  |  |  |  |
| 13 | `EXCHANGERATE` | DECIMAL(6,3) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 16 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 17 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 18 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 19 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 20 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPNEGOTIATIONPC.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NEGOTIATIONCODE,
       t.BANKREFERENCENO,
       t.REFERENCEDATE,
       t.PACKINGCREDITLETTERNO,
       t.BUSINESSUNITCODE,
       t.PACKINGCREDITVALUE,
       t.PACKINGCREDITBALANCEVALUE,
       t.ADJUSTFORTHISBILL,
       t.ADJUSTFCVALUE,
       t.BANKCOMPANYCODE,
       t.BANKCODE
FROM   DB2ADMIN.LOGFINEXPNEGOTIATIONPC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
