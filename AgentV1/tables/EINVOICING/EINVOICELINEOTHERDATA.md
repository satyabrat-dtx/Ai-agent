# DB2ADMIN.EINVOICELINEOTHERDATA

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEGOODSSERVICESLINE`, `OTHERDATAID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237079

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EINVOICEGOODSSERVICESLINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `OTHERDATAID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `SALDOCLINEEIOTHERDATALINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `DATATYPE` | CHAR(10) | NOT NULL |  |  |  |
| 7 | `TEXTREFERENCE` | VARCHAR(120) |  |  |  |  |
| 8 | `NUMBERREFERENCE` | DECIMAL(26,8) |  |  |  |  |
| 9 | `DATEREFERENCE` | DATE |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEGOODSSERVICESDATA_OTHERDATA` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEGOODSSERVICESLINE` | [`EINVOICEGOODSSERVICESDATA`](../EINVOICING/EINVOICEGOODSSERVICESDATA.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `LINENUMBER` | RESTRICT | `EINVOICELINEOTHERDATA.EINVOICEHEADERCOMPANYCODE = EINVOICEGOODSSERVICESDATA.EINVOICEHEADERCOMPANYCODE AND EINVOICELINEOTHERDATA.EINVOICEHEADERUNIQUEID = EINVOICEGOODSSERVICESDATA.EINVOICEHEADERUNIQUEID AND EINVOICELINEOTHERDATA.EINVOICEBODYID = EINVOICEGOODSSERVICESDATA.EINVOICEBODYID AND EINVOICELINEOTHERDATA.EINVOICEGOODSSERVICESLINE = EINVOICEGOODSSERVICESDATA.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICELINEOTHERDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.EINVOICEGOODSSERVICESLINE,
       t.OTHERDATAID,
       t.SALDOCLINEEIOTHERDATALINE,
       t.DATATYPE,
       t.TEXTREFERENCE,
       t.NUMBERREFERENCE,
       t.DATEREFERENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.EINVOICELINEOTHERDATA t
FETCH FIRST 100 ROWS ONLY;
```
