# DB2ADMIN.NOBDEFAULTFORAVAILABILITY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10545

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DAYSWHENAVAILABLE` | INTEGER | NOT NULL |  |  |  |
| 2 | `DAYSWHENUNAVAILABLE` | INTEGER | NOT NULL |  |  |  |
| 3 | `AVAILABILITYFORMULACODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `WORKINGCALENDARCODE` | CHAR(3) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DAYSWHENAVAILABLE,
       t.DAYSWHENUNAVAILABLE,
       t.AVAILABILITYFORMULACODE,
       t.WORKINGCALENDARCODE
FROM   DB2ADMIN.NOBDEFAULTFORAVAILABILITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
