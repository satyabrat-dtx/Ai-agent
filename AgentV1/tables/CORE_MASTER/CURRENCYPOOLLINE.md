# DB2ADMIN.CURRENCYPOOLLINE

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'CURRENCY')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CURRENCYPOOLCOMPANYCODE`, `CURRENCYPOOLCODE`, `LINENR`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198033

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CURRENCYPOOLCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CURRENCYPOOLCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENR` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `FOREIGNAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 4 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 5 | `RESIDUALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `STATUS` | CHAR(1) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `INTERNALNOTE` | VARCHAR(3000) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCYPOOL_LINE` | `CURRENCYPOOLCOMPANYCODE`, `CURRENCYPOOLCODE` | [`CURRENCYPOOL`](../CORE_MASTER/CURRENCYPOOL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CURRENCYPOOLLINE.CURRENCYPOOLCOMPANYCODE = CURRENCYPOOL.COMPANYCODE AND CURRENCYPOOLLINE.CURRENCYPOOLCODE = CURRENCYPOOL.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CURRENCYPOOLLINE_DETAIL` | [`CURRENCYPOOLDETAIL`](../CORE_MASTER/CURRENCYPOOLDETAIL.md) | `CURPOOLLINECURPOOLCOMPANYCODE`, `CURPOOLLINECURRENCYPOOLCODE`, `CURRENCYPOOLLINELINENR` | `CURRENCYPOOLDETAIL.CURPOOLLINECURPOOLCOMPANYCODE = CURRENCYPOOLLINE.CURRENCYPOOLCOMPANYCODE AND CURRENCYPOOLDETAIL.CURPOOLLINECURRENCYPOOLCODE = CURRENCYPOOLLINE.CURRENCYPOOLCODE AND CURRENCYPOOLDETAIL.CURRENCYPOOLLINELINENR = CURRENCYPOOLLINE.LINENR` |

## Indexes

- `CURRENCYPOOLLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CURRENCYPOOLCOMPANYCODE,
       t.CURRENCYPOOLCODE,
       t.LINENR,
       t.FOREIGNAMOUNT,
       t.EXCHANGERATE,
       t.RESIDUALAMOUNT,
       t.STATUS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.CURRENCYPOOLLINE t
FETCH FIRST 100 ROWS ONLY;
```
