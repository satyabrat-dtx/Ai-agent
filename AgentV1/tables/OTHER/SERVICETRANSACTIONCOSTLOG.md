# DB2ADMIN.SERVICETRANSACTIONCOSTLOG

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COMPANYCODE`, `SERVICETRANSACTIONNUMBER`, `SERVICETRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111638

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SERVICETRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `SERVICETRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `TOBEHANDLE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SERVICETRANSACTIONCOSTLOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SERVICETRANSACTIONNUMBER,
       t.SERVICETRANSACTIONDETAILNUMBER,
       t.TOBEHANDLE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SERVICETRANSACTIONCOSTLOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
