# DB2ADMIN.SCDM_BALANCE_HEADER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `BH_IDENTIFIER`, `BH_TABLE_INDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187837

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `BH_TYPE_PROD` | VARCHAR(3) | NOT NULL |  |  |  |
| 2 | `BH_PRODUCT_CODE` | VARCHAR(120) | NOT NULL |  |  |  |
| 3 | `BH_NET_GROUP_CODE` | VARCHAR(16) | NOT NULL |  |  |  |
| 4 | `BH_DUE_DATE` | TIMESTAMP | NOT NULL |  |  |  |
| 5 | `BH_QTY` | DECIMAL(11,2) |  |  |  |  |
| 6 | `BH_INFO_AREA` | VARCHAR(120) |  |  |  |  |
| 7 | `BH_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 8 | `BH_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 9 | `BH_ORIG_DUE_DATE` | TIMESTAMP |  |  |  |  |
| 10 | `BH_TABLE_INDEX` | INTEGER | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCDM_BALANCE_HEADER` (BH_TYPE_PROD, BH_PRODUCT_CODE, BH_NET_GROUP_CODE, BH_DUE_DATE)

## Starter query

```sql
SELECT t.BH_IDENTIFIER,
       t.BH_TYPE_PROD,
       t.BH_PRODUCT_CODE,
       t.BH_NET_GROUP_CODE,
       t.BH_DUE_DATE,
       t.BH_QTY,
       t.BH_INFO_AREA,
       t.BH_USR_NAMECG,
       t.BH_USR_TIMECG,
       t.BH_ORIG_DUE_DATE,
       t.BH_TABLE_INDEX
FROM   DB2ADMIN.SCDM_BALANCE_HEADER t
FETCH FIRST 100 ROWS ONLY;
```
