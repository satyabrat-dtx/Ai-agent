# DB2ADMIN.QACERTIFICATECOMMENTSCKDETAIL

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `QACERCOMCKCOMPANYCODE`, `QACERCOMCKCODE`, `QACERCOMCKSEQUENCE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192710

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QACERCOMCKCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `QACERCOMCKCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `QACERCOMCKSEQUENCE` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SUBCODE01CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE02CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SUBCODE03CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODE04CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBCODE05CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBCODE06CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE07CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SUBCODE08CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SUBCODE09CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `SUBCODE10CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QACERTIFICATECOMMENTSCKDETAIL.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QACERTIFICATECOMMENTSCKDETAIL.ITEMTYPECODE = ITEMTYPE.CODE` |
| `QACERTIFICATECOMMENTSCHSKEYS_DETAILS` | `QACERCOMCKCOMPANYCODE`, `QACERCOMCKCODE`, `QACERCOMCKSEQUENCE` | [`QACERTIFICATECOMMENTSCHSKEYS`](../QUALITY/QACERTIFICATECOMMENTSCHSKEYS.md) | `QACERCOMCKHEACOMPANYCODE`, `QACERCOMCKHEACODE`, `SEQUENCE` | RESTRICT | `QACERTIFICATECOMMENTSCKDETAIL.QACERCOMCKCOMPANYCODE = QACERTIFICATECOMMENTSCHSKEYS.QACERCOMCKHEACOMPANYCODE AND QACERTIFICATECOMMENTSCKDETAIL.QACERCOMCKCODE = QACERTIFICATECOMMENTSCHSKEYS.QACERCOMCKHEACODE AND QACERTIFICATECOMMENTSCKDETAIL.QACERCOMCKSEQUENCE = QACERTIFICATECOMMENTSCHSKEYS.SEQUENCE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ERTIFICATECOMMENTSCKDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.QACERCOMCKCOMPANYCODE,
       t.QACERCOMCKCODE,
       t.QACERCOMCKSEQUENCE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01CONTROLLED,
       t.SUBCODE02CONTROLLED,
       t.SUBCODE03CONTROLLED,
       t.SUBCODE04CONTROLLED,
       t.SUBCODE05CONTROLLED,
       t.SUBCODE06CONTROLLED,
       t.SUBCODE07CONTROLLED
FROM   DB2ADMIN.QACERTIFICATECOMMENTSCKDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
