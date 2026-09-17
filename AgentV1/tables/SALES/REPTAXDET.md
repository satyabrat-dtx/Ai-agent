# DB2ADMIN.REPTAXDET

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `REPORTTAXCOMPANYCODE`, `REPORTTAXDIVISIONCODE`, `REPORTTAXCODE`, `SEQNO`, `LINENO`, `TAXNAME`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123367

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORTTAXCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `REPORTTAXDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `REPORTTAXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQNO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `TAXNAME` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `REPORTTAX_LINE` | `REPORTTAXCOMPANYCODE`, `REPORTTAXDIVISIONCODE`, `REPORTTAXCODE` | [`REPORTTAX`](../OTHER/REPORTTAX.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `REPTAXDET.REPORTTAXCOMPANYCODE = REPORTTAX.COMPANYCODE AND REPTAXDET.REPORTTAXDIVISIONCODE = REPORTTAX.DIVISIONCODE AND REPTAXDET.REPORTTAXCODE = REPORTTAX.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `REPTAXDET_LINE` | [`RTDDETAIL`](../SALES/RTDDETAIL.md) | `REPTAXDETREPORTTAXCOMPANYCODE`, `REPTAXDETREPORTTAXDIVISIONCODE`, `REPTAXDETREPORTTAXCODE`, `REPTAXDETSEQNO`, `REPTAXDETLINENO`, `REPTAXDETTAXNAME` | `RTDDETAIL.REPTAXDETREPORTTAXCOMPANYCODE = REPTAXDET.REPORTTAXCOMPANYCODE AND RTDDETAIL.REPTAXDETREPORTTAXDIVISIONCODE = REPTAXDET.REPORTTAXDIVISIONCODE AND RTDDETAIL.REPTAXDETREPORTTAXCODE = REPTAXDET.REPORTTAXCODE AND RTDDETAIL.REPTAXDETSEQNO = REPTAXDET.SEQNO AND RTDDETAIL.REPTAXDETLINENO = REPTAXDET.LINENO AND RTDDETAIL.REPTAXDETTAXNAME = REPTAXDET.TAXNAME` |

## Indexes

- `REPTAXDETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.REPORTTAXCOMPANYCODE,
       t.REPORTTAXDIVISIONCODE,
       t.REPORTTAXCODE,
       t.SEQNO,
       t.LINENO,
       t.TAXNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.REPTAXDET t
FETCH FIRST 100 ROWS ONLY;
```
