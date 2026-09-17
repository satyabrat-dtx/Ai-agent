# DB2ADMIN.QACERTIFICATECOMMENTSCHSKEYS

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `QACERCOMCKHEACOMPANYCODE`, `QACERCOMCKHEACODE`, `SEQUENCE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192664

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QACERCOMCKHEACOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `QACERCOMCKHEACODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 3 | `QUALITYCERTIFICATETMPCTD` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ITEMTYPECONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ITEMCONTROLLED` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `ORDERPARTNERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `PROTOTYPECONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `QACERTIFICATECOMMENTSCKHEADER_QACERTIFICATECOMMENTSCHOOSEKEYS` | `QACERCOMCKHEACOMPANYCODE`, `QACERCOMCKHEACODE` | [`QACERTIFICATECOMMENTSCKHEADER`](../QUALITY/QACERTIFICATECOMMENTSCKHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QACERTIFICATECOMMENTSCHSKEYS.QACERCOMCKHEACOMPANYCODE = QACERTIFICATECOMMENTSCKHEADER.COMPANYCODE AND QACERTIFICATECOMMENTSCHSKEYS.QACERCOMCKHEACODE = QACERTIFICATECOMMENTSCKHEADER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QACERTIFICATECOMMENTSCHSKEYS_DETAILS` | [`QACERTIFICATECOMMENTSCKDETAIL`](../QUALITY/QACERTIFICATECOMMENTSCKDETAIL.md) | `QACERCOMCKCOMPANYCODE`, `QACERCOMCKCODE`, `QACERCOMCKSEQUENCE` | `QACERTIFICATECOMMENTSCKDETAIL.QACERCOMCKCOMPANYCODE = QACERTIFICATECOMMENTSCHSKEYS.QACERCOMCKHEACOMPANYCODE AND QACERTIFICATECOMMENTSCKDETAIL.QACERCOMCKCODE = QACERTIFICATECOMMENTSCHSKEYS.QACERCOMCKHEACODE AND QACERTIFICATECOMMENTSCKDETAIL.QACERCOMCKSEQUENCE = QACERTIFICATECOMMENTSCHSKEYS.SEQUENCE` |

## Indexes

- `ERTIFICATECOMMENTSCHSKEYSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.QACERCOMCKHEACOMPANYCODE,
       t.QACERCOMCKHEACODE,
       t.SEQUENCE,
       t.QUALITYCERTIFICATETMPCTD,
       t.ITEMTYPECONTROLLED,
       t.ITEMCONTROLLED,
       t.ORDERPARTNERCONTROLLED,
       t.ABSUNIQUEID,
       t.PROTOTYPECONTROLLED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.QACERTIFICATECOMMENTSCHSKEYS t
FETCH FIRST 100 ROWS ONLY;
```
