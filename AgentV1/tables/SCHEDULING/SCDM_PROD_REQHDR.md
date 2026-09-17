# DB2ADMIN.SCDM_PROD_REQHDR

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `PH_IDENTIFIER`, `PH_PREQ_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186515

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PH_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PH_UPD_CODE` | INTEGER | NOT NULL |  |  |  |
| 3 | `PH_HISTORICAL_REQ` | CHAR(1) |  |  |  |  |
| 4 | `PH_REQ_ORIGIN` | VARCHAR(2) |  |  |  |  |
| 5 | `PH_PROD_LINE` | VARCHAR(4) |  |  |  |  |
| 6 | `PH_TYPE_PROD` | VARCHAR(3) |  |  |  |  |
| 7 | `PH_PROD_FAMILY` | VARCHAR(120) |  |  |  |  |
| 8 | `PH_MATERIAL_FAMILY` | VARCHAR(120) |  |  |  |  |
| 9 | `PH_PROD_UM` | VARCHAR(3) |  |  |  |  |
| 10 | `PH_PROD_LOW_TIME_STRT` | TIMESTAMP |  |  |  |  |
| 11 | `PH_PROD_DELIVY_DATE` | TIMESTAMP |  |  |  |  |
| 12 | `PH_FRC_DEL_DATE` | CHAR(1) |  |  |  |  |
| 13 | `PH_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 14 | `PH_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 15 | `PH_MODULEHANDLE` | CHAR(1) |  |  |  |  |
| 16 | `PH_SPLITCONFLEVELS` | CHAR(1) |  |  |  |  |
| 17 | `PH_LEAD_STEP_SPLITED` | SMALLINT |  |  |  |  |
| 18 | `PH_NEW_PREQ_UNIQ_ID` | VARCHAR(10) |  |  |  |  |
| 19 | `PH_SERVING_CODE` | VARCHAR(25) |  |  |  |  |
| 20 | `PH_SERVED_CODE` | VARCHAR(25) |  |  |  |  |
| 21 | `PH_CURVE_FAMILY_ID_CODE` | VARCHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCDM_PROD_REQHDR` (PH_IDENTIFIER, PH_SERVING_CODE)

## Starter query

```sql
SELECT t.PH_IDENTIFIER,
       t.PH_PREQ_NO,
       t.PH_UPD_CODE,
       t.PH_HISTORICAL_REQ,
       t.PH_REQ_ORIGIN,
       t.PH_PROD_LINE,
       t.PH_TYPE_PROD,
       t.PH_PROD_FAMILY,
       t.PH_MATERIAL_FAMILY,
       t.PH_PROD_UM,
       t.PH_PROD_LOW_TIME_STRT,
       t.PH_PROD_DELIVY_DATE
FROM   DB2ADMIN.SCDM_PROD_REQHDR t
FETCH FIRST 100 ROWS ONLY;
```
