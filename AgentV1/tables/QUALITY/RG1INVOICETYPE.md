# DB2ADMIN.RG1INVOICETYPE

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `RG1SEQDEFRG1TMPCOMPANYCODE`, `RG1SEQDEFRG1TMPDIVISIONCODE`, `RG1SEQDEFRG1TEMPLATECODE`, `RG1SEQDEFSEQNO`, `RG1SEQDEFEFFECTIVEFROMDATE`, `INVOICETYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142343

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RG1SEQDEFRG1TMPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RG1SEQDEFRG1TMPDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RG1SEQDEFRG1TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RG1SEQDEFSEQNO` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `RG1SEQDEFEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RG1SEQDEF_INVOICETYPE` | `RG1SEQDEFRG1TMPCOMPANYCODE`, `RG1SEQDEFRG1TMPDIVISIONCODE`, `RG1SEQDEFRG1TEMPLATECODE`, `RG1SEQDEFSEQNO`, `RG1SEQDEFEFFECTIVEFROMDATE` | [`RG1SEQDEF`](../QUALITY/RG1SEQDEF.md) | `RG1TEMPLATECOMPANYCODE`, `RG1TEMPLATEDIVISIONCODE`, `RG1TEMPLATECODE`, `SEQNO`, `EFFECTIVEFROMDATE` | RESTRICT | `RG1INVOICETYPE.RG1SEQDEFRG1TMPCOMPANYCODE = RG1SEQDEF.RG1TEMPLATECOMPANYCODE AND RG1INVOICETYPE.RG1SEQDEFRG1TMPDIVISIONCODE = RG1SEQDEF.RG1TEMPLATEDIVISIONCODE AND RG1INVOICETYPE.RG1SEQDEFRG1TEMPLATECODE = RG1SEQDEF.RG1TEMPLATECODE AND RG1INVOICETYPE.RG1SEQDEFSEQNO = RG1SEQDEF.SEQNO AND RG1INVOICETYPE.RG1SEQDEFEFFECTIVEFROMDATE = RG1SEQDEF.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG1INVOICETYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RG1SEQDEFRG1TMPCOMPANYCODE,
       t.RG1SEQDEFRG1TMPDIVISIONCODE,
       t.RG1SEQDEFRG1TEMPLATECODE,
       t.RG1SEQDEFSEQNO,
       t.RG1SEQDEFEFFECTIVEFROMDATE,
       t.INVOICETYPECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.RG1INVOICETYPE t
FETCH FIRST 100 ROWS ONLY;
```
