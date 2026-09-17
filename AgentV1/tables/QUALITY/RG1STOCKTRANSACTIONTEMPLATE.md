# DB2ADMIN.RG1STOCKTRANSACTIONTEMPLATE

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `RG1SEQDEFRG1TMPCOMPANYCODE`, `RG1SEQDEFRG1TMPDIVISIONCODE`, `RG1SEQDEFRG1TEMPLATECODE`, `RG1SEQDEFSEQNO`, `RG1SEQDEFEFFECTIVEFROMDATE`, `LOGICALWAREHOUSECODE`, `ITEMTYPECODE`, `STOCKTRANSACTIONTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142442

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RG1SEQDEFRG1TMPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RG1SEQDEFRG1TMPDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RG1SEQDEFRG1TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RG1SEQDEFSEQNO` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `RG1SEQDEFEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RG1SEQDEF_STOCKTRANSACTIONTEMPLATE` | `RG1SEQDEFRG1TMPCOMPANYCODE`, `RG1SEQDEFRG1TMPDIVISIONCODE`, `RG1SEQDEFRG1TEMPLATECODE`, `RG1SEQDEFSEQNO`, `RG1SEQDEFEFFECTIVEFROMDATE` | [`RG1SEQDEF`](../QUALITY/RG1SEQDEF.md) | `RG1TEMPLATECOMPANYCODE`, `RG1TEMPLATEDIVISIONCODE`, `RG1TEMPLATECODE`, `SEQNO`, `EFFECTIVEFROMDATE` | RESTRICT | `RG1STOCKTRANSACTIONTEMPLATE.RG1SEQDEFRG1TMPCOMPANYCODE = RG1SEQDEF.RG1TEMPLATECOMPANYCODE AND RG1STOCKTRANSACTIONTEMPLATE.RG1SEQDEFRG1TMPDIVISIONCODE = RG1SEQDEF.RG1TEMPLATEDIVISIONCODE AND RG1STOCKTRANSACTIONTEMPLATE.RG1SEQDEFRG1TEMPLATECODE = RG1SEQDEF.RG1TEMPLATECODE AND RG1STOCKTRANSACTIONTEMPLATE.RG1SEQDEFSEQNO = RG1SEQDEF.SEQNO AND RG1STOCKTRANSACTIONTEMPLATE.RG1SEQDEFEFFECTIVEFROMDATE = RG1SEQDEF.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG1STOCKTRNTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RG1SEQDEFRG1TMPCOMPANYCODE,
       t.RG1SEQDEFRG1TMPDIVISIONCODE,
       t.RG1SEQDEFRG1TEMPLATECODE,
       t.RG1SEQDEFSEQNO,
       t.RG1SEQDEFEFFECTIVEFROMDATE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.STOCKTRNTEMPLATECOMPANYCODE,
       t.STOCKTRANSACTIONTEMPLATECODE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.RG1STOCKTRANSACTIONTEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
