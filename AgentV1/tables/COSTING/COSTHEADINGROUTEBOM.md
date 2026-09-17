# DB2ADMIN.COSTHEADINGROUTEBOM

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2743

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 3 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 4 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 5 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `ROUTINGINDEX` | DECIMAL(11,0) |  |  |  |  |
| 7 | `BOMINDEX` | DECIMAL(11,0) |  |  |  |  |
| 8 | `ROUTINGINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `COSTINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `GOODSVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 13 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTHEADINGROUTEBOMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTINGINDEX,
       t.BOMINDEX,
       t.ROUTINGINCIDENCE,
       t.BOMINCIDENCE,
       t.COSTINBASECURRENCY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COSTHEADINGROUTEBOM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
