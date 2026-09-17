# DB2ADMIN.EINVOICEATTACHMENT

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `ATTACHMENTID`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236370

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ATTACHMENTID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `NAME` | VARCHAR(120) | NOT NULL |  |  |  |
| 5 | `COMPRESSION` | CHAR(10) |  |  |  |  |
| 6 | `FORMAT` | CHAR(10) |  |  |  |  |
| 7 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 8 | `ATTACHMENTFILEPATH` | VARCHAR(255) |  |  |  |  |
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
| `EINVOICEBODY_ATTACHMENT` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `BODYID` | RESTRICT | `EINVOICEATTACHMENT.EINVOICEHEADERCOMPANYCODE = EINVOICEBODY.EINVOICEHEADERCOMPANYCODE AND EINVOICEATTACHMENT.EINVOICEHEADERUNIQUEID = EINVOICEBODY.EINVOICEHEADERUNIQUEID AND EINVOICEATTACHMENT.EINVOICEBODYID = EINVOICEBODY.BODYID` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EINVOICEATTACHMENT_SPLITDATA` | [`EINVOICEATTACHMENTDATA`](../EINVOICING/EINVOICEATTACHMENTDATA.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEATTACHMENTATTACHMENTID` | `EINVOICEATTACHMENTDATA.EINVOICEHEADERCOMPANYCODE = EINVOICEATTACHMENT.EINVOICEHEADERCOMPANYCODE AND EINVOICEATTACHMENTDATA.EINVOICEHEADERUNIQUEID = EINVOICEATTACHMENT.EINVOICEHEADERUNIQUEID AND EINVOICEATTACHMENTDATA.EINVOICEBODYID = EINVOICEATTACHMENT.EINVOICEBODYID AND EINVOICEATTACHMENTDATA.EINVOICEATTACHMENTATTACHMENTID = EINVOICEATTACHMENT.ATTACHMENTID` |

## Indexes

- `EINVOICEATTACHMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.ATTACHMENTID,
       t.NAME,
       t.COMPRESSION,
       t.FORMAT,
       t.DESCRIPTION,
       t.ATTACHMENTFILEPATH,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.EINVOICEATTACHMENT t
FETCH FIRST 100 ROWS ONLY;
```
