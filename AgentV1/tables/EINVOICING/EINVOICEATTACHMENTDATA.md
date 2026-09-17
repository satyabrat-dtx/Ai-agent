# DB2ADMIN.EINVOICEATTACHMENTDATA

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEATTACHMENTATTACHMENTID`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236418

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EINVOICEATTACHMENTATTACHMENTID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `DATA` | BLOB(1000000) | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEATTACHMENT_SPLITDATA` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEATTACHMENTATTACHMENTID` | [`EINVOICEATTACHMENT`](../EINVOICING/EINVOICEATTACHMENT.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `ATTACHMENTID` | RESTRICT | `EINVOICEATTACHMENTDATA.EINVOICEHEADERCOMPANYCODE = EINVOICEATTACHMENT.EINVOICEHEADERCOMPANYCODE AND EINVOICEATTACHMENTDATA.EINVOICEHEADERUNIQUEID = EINVOICEATTACHMENT.EINVOICEHEADERUNIQUEID AND EINVOICEATTACHMENTDATA.EINVOICEBODYID = EINVOICEATTACHMENT.EINVOICEBODYID AND EINVOICEATTACHMENTDATA.EINVOICEATTACHMENTATTACHMENTID = EINVOICEATTACHMENT.ATTACHMENTID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEATTACHMENTDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.EINVOICEATTACHMENTATTACHMENTID,
       t.SEQUENCE,
       t.DATA,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EINVOICEATTACHMENTDATA t
FETCH FIRST 100 ROWS ONLY;
```
