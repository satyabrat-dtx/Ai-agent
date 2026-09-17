# DB2ADMIN.COSTHEADINGROUTEBOMBYDATE

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `PRODUCTINDEX`, `PLANTCODE`, `COSTGROUPCODE`, `COSTSCOSTGROUPCODE`, `VALIDITYDATE`, `ROUTINGINDEX`, `BOMINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238134

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `VALIDITYDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `ROUTINGINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 7 | `BOMINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 8 | `ROUTINGINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `COSTINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 11 | `GOODSVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 12 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTHEADINGROUTEBOMBYDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.VALIDITYDATE,
       t.ROUTINGINDEX,
       t.BOMINDEX,
       t.ROUTINGINCIDENCE,
       t.BOMINCIDENCE,
       t.COSTINBASECURRENCY,
       t.GOODSVALUEINBASECURRENCY
FROM   DB2ADMIN.COSTHEADINGROUTEBOMBYDATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
