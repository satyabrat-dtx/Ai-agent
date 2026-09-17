# DB2ADMIN.SCDA_ITEMTYPELOGICALWAREHOUSE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `IDENTIFIER`, `ITEMTYPECODE`, `LOGICALWAREHOUSECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185365

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ITEMTYPECODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `LOGICALWAREHOUSECODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `RESERVATIONTABLENAME` | VARCHAR(30) |  |  |  |  |
| 4 | `RESERVATIONCOLUMNNAME` | VARCHAR(30) |  |  |  |  |
| 5 | `DEMANDTABLENAME` | VARCHAR(30) |  |  |  |  |
| 6 | `DEMANDCOLUMNNAME` | VARCHAR(30) |  |  |  |  |
| 7 | `CONN_BTW_STOCK_AND_RESRV` | CHAR(1) |  |  |  |  |
| 8 | `SEPARATE_BTW_ATTRIBUTE` | CHAR(1) |  |  |  |  |
| 9 | `IW_1ST_COLUMN` | VARCHAR(50) |  |  |  |  |
| 10 | `DSP_BEFORE_2ST_COLUMN` | CHAR(1) |  |  |  |  |
| 11 | `IW_2ST_COLUMN` | VARCHAR(50) |  |  |  |  |
| 12 | `DSP_BEFORE_3ST_COLUMN` | CHAR(1) |  |  |  |  |
| 13 | `IW_3ST_COLUMN` | VARCHAR(50) |  |  |  |  |
| 14 | `DSP_BEFORE_4ST_COLUMN` | CHAR(1) |  |  |  |  |
| 15 | `IW_4ST_COLUMN` | VARCHAR(50) |  |  |  |  |
| 16 | `DSP_BEFORE_5ST_COLUMN` | CHAR(1) |  |  |  |  |
| 17 | `IW_5ST_COLUMN` | VARCHAR(50) |  |  |  |  |
| 18 | `DSP_BEFORE_6ST_COLUMN` | CHAR(1) |  |  |  |  |
| 19 | `IW_6ST_COLUMN` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECODE,
       t.RESERVATIONTABLENAME,
       t.RESERVATIONCOLUMNNAME,
       t.DEMANDTABLENAME,
       t.DEMANDCOLUMNNAME,
       t.CONN_BTW_STOCK_AND_RESRV,
       t.SEPARATE_BTW_ATTRIBUTE,
       t.IW_1ST_COLUMN,
       t.DSP_BEFORE_2ST_COLUMN,
       t.IW_2ST_COLUMN
FROM   DB2ADMIN.SCDA_ITEMTYPELOGICALWAREHOUSE t
FETCH FIRST 100 ROWS ONLY;
```
