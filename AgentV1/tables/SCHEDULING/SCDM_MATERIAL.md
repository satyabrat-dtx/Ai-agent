# DB2ADMIN.SCDM_MATERIAL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `no_primary_key`
- **Columns**: 21
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187629

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MT_IDENTIFIER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `MT_PREQ_NO` | VARCHAR(30) | NOT NULL |  |  |  |
| 2 | `MT_PSTEP_ID` | SMALLINT | NOT NULL |  |  |  |
| 3 | `MT_ORG_STEP` | SMALLINT | NOT NULL |  |  |  |
| 4 | `MT_WKCNTER` | VARCHAR(8) | NOT NULL |  |  |  |
| 5 | `MT_RES_CAT_CODE` | VARCHAR(3) | NOT NULL |  |  |  |
| 6 | `MT_RSC_CODE` | VARCHAR(8) | NOT NULL |  |  |  |
| 7 | `MT_MACHINE_SETUP_CODE` | VARCHAR(10) | NOT NULL |  |  |  |
| 8 | `MT_ALTERNATIVE_CODE` | VARCHAR(6) | NOT NULL |  |  |  |
| 9 | `MT_TYPE_PROD` | VARCHAR(3) | NOT NULL |  |  |  |
| 10 | `MT_PRODUCT_CODE` | VARCHAR(120) | NOT NULL |  |  |  |
| 11 | `MT_NET_GROUP_CODE` | VARCHAR(16) | NOT NULL |  |  |  |
| 12 | `MT_ISSUE_CODE` | VARCHAR(6) | NOT NULL |  |  |  |
| 13 | `MT_SEQ_ISSUED` | VARCHAR(3) | NOT NULL |  |  |  |
| 14 | `MT_MAT_BALANCE` | CHAR(1) |  |  |  |  |
| 15 | `MT_QTY_ALLOC` | DECIMAL(11,2) |  |  |  |  |
| 16 | `MT_HIGH_DATE_ALLOC` | TIMESTAMP |  |  |  |  |
| 17 | `MT_SEARCH_MAT_ALLOC` | CHAR(1) |  |  |  |  |
| 18 | `MT_SETTLED` | CHAR(1) |  |  |  |  |
| 19 | `MT_QUANTITY_ISSUE` | DECIMAL(11,2) |  |  |  |  |
| 20 | `MT_REQ_QUANTITY` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCDM_MATERIAL` (MT_TYPE_PROD, MT_PRODUCT_CODE)
- `SCDM_MATERIALBYREQ` (MT_PREQ_NO, MT_PSTEP_ID)

## Starter query

```sql
SELECT t.MT_IDENTIFIER,
       t.MT_PREQ_NO,
       t.MT_PSTEP_ID,
       t.MT_ORG_STEP,
       t.MT_WKCNTER,
       t.MT_RES_CAT_CODE,
       t.MT_RSC_CODE,
       t.MT_MACHINE_SETUP_CODE,
       t.MT_ALTERNATIVE_CODE,
       t.MT_TYPE_PROD,
       t.MT_PRODUCT_CODE,
       t.MT_NET_GROUP_CODE
FROM   DB2ADMIN.SCDM_MATERIAL t
FETCH FIRST 100 ROWS ONLY;
```
