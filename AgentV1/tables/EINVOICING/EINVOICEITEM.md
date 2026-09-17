# DB2ADMIN.EINVOICEITEM

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEGOODSSERVICESLINE`, `ITEMID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236983

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EINVOICEGOODSSERVICESLINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITEMID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ITEMTYPE` | CHAR(70) | NOT NULL |  |  |  |
| 6 | `ITEMVALUE` | CHAR(70) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEGOODSSERVICESDATA_ITEM` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEGOODSSERVICESLINE` | [`EINVOICEGOODSSERVICESDATA`](../EINVOICING/EINVOICEGOODSSERVICESDATA.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `LINENUMBER` | RESTRICT | `EINVOICEITEM.EINVOICEHEADERCOMPANYCODE = EINVOICEGOODSSERVICESDATA.EINVOICEHEADERCOMPANYCODE AND EINVOICEITEM.EINVOICEHEADERUNIQUEID = EINVOICEGOODSSERVICESDATA.EINVOICEHEADERUNIQUEID AND EINVOICEITEM.EINVOICEBODYID = EINVOICEGOODSSERVICESDATA.EINVOICEBODYID AND EINVOICEITEM.EINVOICEGOODSSERVICESLINE = EINVOICEGOODSSERVICESDATA.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEITEMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.EINVOICEGOODSSERVICESLINE,
       t.ITEMID,
       t.ITEMTYPE,
       t.ITEMVALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.EINVOICEITEM t
FETCH FIRST 100 ROWS ONLY;
```
