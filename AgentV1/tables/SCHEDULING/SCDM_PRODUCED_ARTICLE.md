# DB2ADMIN.SCDM_PRODUCED_ARTICLE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `PA_IDENTIFIER`, `PA_PREQ_NO`, `PA_SEQUENCE`, `PA_PRODUCT_CODE`, `PA_NET_GROUP_CODE`, `PA_ALLOC_REQ`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187769

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PA_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PA_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PA_SEQUENCE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `PA_PRODUCT_CODE` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `PA_NET_GROUP_CODE` | VARCHAR(16) | NOT NULL | PK | primary_key |  |
| 5 | `PA_ALLOC_REQ` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 6 | `PA_PROD_BALANCE` | CHAR(1) |  |  |  |  |
| 7 | `PA_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 8 | `PA_SETTLED` | CHAR(1) |  |  |  |  |
| 9 | `PA_REQ_QUANTITY` | DECIMAL(11,2) |  |  |  |  |
| 10 | `PA_QTY_PRODUCED` | DECIMAL(11,2) |  |  |  |  |
| 11 | `PA_QTY_ALLOC` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PA_IDENTIFIER,
       t.PA_PREQ_NO,
       t.PA_SEQUENCE,
       t.PA_PRODUCT_CODE,
       t.PA_NET_GROUP_CODE,
       t.PA_ALLOC_REQ,
       t.PA_PROD_BALANCE,
       t.PA_RSC_CODE,
       t.PA_SETTLED,
       t.PA_REQ_QUANTITY,
       t.PA_QTY_PRODUCED,
       t.PA_QTY_ALLOC
FROM   DB2ADMIN.SCDM_PRODUCED_ARTICLE t
FETCH FIRST 100 ROWS ONLY;
```
