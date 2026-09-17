# DB2ADMIN.SALESDOCUMENTIMPORTERROR

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27013

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `HEADERIMPORTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `HDRIMPIMPORTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 3 | `LINEIMPORTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 4 | `LINEIMPORTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 5 | `LINEIMPORTCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 6 | `DISCOUNTIMPORTIMPORTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 7 | `CHARGEIMPORTIMPORTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 8 | `COMMENTIMPORTCODE` | CHAR(12) |  |  |  |  |
| 9 | `LINEDSCIMPORTIMPORTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 10 | `LINECOMMISSIONIMPORTAGENTCODE` | CHAR(3) |  |  |  |  |
| 11 | `LINECMSIMPORTIMPORTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 12 | `LINECHARGEIMPORTIMPORTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 13 | `LINECOMMENTIMPORTCODE` | CHAR(12) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTIMPORTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.HEADERIMPORTCOMPANYCODE,
       t.HDRIMPIMPORTPROVISIONALCODE,
       t.LINEIMPORTORDERLINE,
       t.LINEIMPORTORDERSUBLINE,
       t.LINEIMPORTCOMPONENTORDERLINE,
       t.DISCOUNTIMPORTIMPORTNUMBERID,
       t.CHARGEIMPORTIMPORTNUMBERID,
       t.COMMENTIMPORTCODE,
       t.LINEDSCIMPORTIMPORTNUMBERID,
       t.LINECOMMISSIONIMPORTAGENTCODE,
       t.LINECMSIMPORTIMPORTNUMBERID
FROM   DB2ADMIN.SALESDOCUMENTIMPORTERROR t
FETCH FIRST 100 ROWS ONLY;
```
