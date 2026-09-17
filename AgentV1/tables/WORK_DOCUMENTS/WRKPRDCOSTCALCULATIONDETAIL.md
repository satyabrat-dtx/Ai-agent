# DB2ADMIN.WRKPRDCOSTCALCULATIONDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `UNIQUEID`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 6087

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TABLEINDEX` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 2 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 3 | `ROUTINGINDEX` | DECIMAL(11,0) |  |  |  |  |
| 4 | `BOMINDEX` | DECIMAL(11,0) |  |  |  |  |
| 5 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 7 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 10 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 11 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 12 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 13 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 14 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 15 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 16 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 17 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 18 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 19 | `RUNNINGDATE` | DATE |  |  |  |  |
| 20 | `PRIORITY` | BIGINT | NOT NULL |  |  |  |
| 21 | `ISFATHER` | SMALLINT | NOT NULL |  |  |  |
| 22 | `CALCULATED` | SMALLINT | NOT NULL |  |  |  |
| 23 | `LEVELED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 25 | `ENDCALCULATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 27 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPRDCALCDTL01` (UNIQUEID, PLANTCODE, COSTGROUPCODE, COSTSCOSTGROUPCODE, PRODUCTINDEX)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.TABLEINDEX,
       t.PRODUCTINDEX,
       t.ROUTINGINDEX,
       t.BOMINDEX,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.PLANTCODE,
       t.ITEMTYPECODE,
       t.PRODUCTSUBCODE01,
       t.PRODUCTSUBCODE02,
       t.PRODUCTSUBCODE03
FROM   DB2ADMIN.WRKPRDCOSTCALCULATIONDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
