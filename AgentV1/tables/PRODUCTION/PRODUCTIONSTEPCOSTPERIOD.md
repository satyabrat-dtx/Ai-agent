# DB2ADMIN.PRODUCTIONSTEPCOSTPERIOD

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PROSTEPCOSTPROCOSTCOMPANYCODE`, `PROSTEPCOSTPROCOSTCOUNTERCODE`, `PROSTEPCOSTPRODUCTIONCOSTCODE`, `PROSTEPCOSTPROCOSTCOSTNUMBER`, `PRODUCTIONSTEPCOSTSTEPNUMBER`, `PERIODDATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42141

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PROSTEPCOSTPROCOSTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `PROSTEPCOSTPROCOSTCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PROSTEPCOSTPRODUCTIONCOSTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `PROSTEPCOSTPROCOSTCOSTNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `PRODUCTIONSTEPCOSTSTEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `PERIODDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `THEORETICALCOSTSFORDATEPERCE` | DECIMAL(3,2) |  |  |  |  |
| 7 | `THEORETICALCOSTSFORDATEPRC` | DECIMAL(3,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PROSTEPCOSTPROCOSTCOMPANYCODE,
       t.PROSTEPCOSTPROCOSTCOUNTERCODE,
       t.PROSTEPCOSTPRODUCTIONCOSTCODE,
       t.PROSTEPCOSTPROCOSTCOSTNUMBER,
       t.PRODUCTIONSTEPCOSTSTEPNUMBER,
       t.PERIODDATE,
       t.THEORETICALCOSTSFORDATEPERCE,
       t.THEORETICALCOSTSFORDATEPRC
FROM   DB2ADMIN.PRODUCTIONSTEPCOSTPERIOD t
FETCH FIRST 100 ROWS ONLY;
```
