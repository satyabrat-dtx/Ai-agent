# DB2ADMIN.WRKCOSTSIMULATIONDATA

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196644

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SIMULATIONCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `SIMULATIONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ROUTESTEPJSON` | CLOB(1000000000) |  |  |  |  |
| 5 | `COSTHEADINGJSON` | CLOB(1000000000) |  |  |  |  |
| 6 | `COSTHEADINGROUTEBOMJSON` | CLOB(1000000000) |  |  |  |  |
| 7 | `ROUTECONSJSON` | CLOB(1000000000) |  |  |  |  |
| 8 | `COSTSIMPROFITELEMENTSJSON` | CLOB(1000000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SIMULATIONCOUNTERCODE,
       t.SIMULATIONCODE,
       t.LINENUMBER,
       t.ROUTESTEPJSON,
       t.COSTHEADINGJSON,
       t.COSTHEADINGROUTEBOMJSON,
       t.ROUTECONSJSON,
       t.COSTSIMPROFITELEMENTSJSON
FROM   DB2ADMIN.WRKCOSTSIMULATIONDATA t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
