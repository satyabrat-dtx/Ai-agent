# DB2ADMIN.EINVOICELINECHARGEDISCOUNT

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEGOODSSERVICESLINE`, `CHARGEDISCOUNTID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237030

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EINVOICEGOODSSERVICESLINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CHARGEDISCOUNTID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `SALDOCUMENTLINECHARGENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 6 | `TYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `PERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 8 | `VALUE` | DECIMAL(21,8) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEGOODSSERVICESDATA_CHARGEDISCOUNT` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEGOODSSERVICESLINE` | [`EINVOICEGOODSSERVICESDATA`](../EINVOICING/EINVOICEGOODSSERVICESDATA.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `LINENUMBER` | RESTRICT | `EINVOICELINECHARGEDISCOUNT.EINVOICEHEADERCOMPANYCODE = EINVOICEGOODSSERVICESDATA.EINVOICEHEADERCOMPANYCODE AND EINVOICELINECHARGEDISCOUNT.EINVOICEHEADERUNIQUEID = EINVOICEGOODSSERVICESDATA.EINVOICEHEADERUNIQUEID AND EINVOICELINECHARGEDISCOUNT.EINVOICEBODYID = EINVOICEGOODSSERVICESDATA.EINVOICEBODYID AND EINVOICELINECHARGEDISCOUNT.EINVOICEGOODSSERVICESLINE = EINVOICEGOODSSERVICESDATA.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICELINECHARGEDISCOUNTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.EINVOICEGOODSSERVICESLINE,
       t.CHARGEDISCOUNTID,
       t.SALDOCUMENTLINECHARGENUMBERID,
       t.TYPE,
       t.PERCENTAGE,
       t.VALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.EINVOICELINECHARGEDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
