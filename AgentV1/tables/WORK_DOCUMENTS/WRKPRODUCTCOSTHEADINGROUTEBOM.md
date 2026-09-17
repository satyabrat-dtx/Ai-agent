# DB2ADMIN.WRKPRODUCTCOSTHEADINGROUTEBOM

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `UNIQUEID`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19465

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 4 | `RUNNINGDATE` | DATE |  |  |  |  |
| 5 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 6 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 7 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 8 | `ROUTINGINDEX` | DECIMAL(11,0) |  |  |  |  |
| 9 | `BOMINDEX` | DECIMAL(11,0) |  |  |  |  |
| 10 | `ROUTINGINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 11 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `COSTINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 13 | `ENDCALCULATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `GOODSVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 15 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 16 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.UNIQUEID,
       t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.RUNNINGDATE,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTINGINDEX,
       t.BOMINDEX,
       t.ROUTINGINCIDENCE,
       t.BOMINCIDENCE
FROM   DB2ADMIN.WRKPRODUCTCOSTHEADINGROUTEBOM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
