# DB2ADMIN.ISOSPECIFICATION

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 6 of 6 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 6 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 97542

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ISOSPECIFICATION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ISOSPECIFICATION_ISOSPECIFICATION` | [`QUALITYCHARACTERISTICTYPE`](../QUALITY/QUALITYCHARACTERISTICTYPE.md) | `COMPANYCODE`, `ISOSPECIFICATIONCODE` | `QUALITYCHARACTERISTICTYPE.COMPANYCODE = ISOSPECIFICATION.COMPANYCODE AND QUALITYCHARACTERISTICTYPE.ISOSPECIFICATIONCODE = ISOSPECIFICATION.CODE` |
| `ISOSPECIFICATION_ISOSPECIFICATION` | [`QUALITYDOCLINE`](../QUALITY/QUALITYDOCLINE.md) | `QUALITYDOCUMENTCOMPANYCODE`, `ISOSPECIFICATIONCODE` | `QUALITYDOCLINE.QUALITYDOCUMENTCOMPANYCODE = ISOSPECIFICATION.COMPANYCODE AND QUALITYDOCLINE.ISOSPECIFICATIONCODE = ISOSPECIFICATION.CODE` |
| `ISOSPECIFICATION_ISOSPECIFICATION` | [`QUALITYDOCLINEDETAIL`](../QUALITY/QUALITYDOCLINEDETAIL.md) | `QUALITYDOCUMENTCOMPANYCODE`, `ISOSPECIFICATIONCODE` | `QUALITYDOCLINEDETAIL.QUALITYDOCUMENTCOMPANYCODE = ISOSPECIFICATION.COMPANYCODE AND QUALITYDOCLINEDETAIL.ISOSPECIFICATIONCODE = ISOSPECIFICATION.CODE` |
| `ISOSPECIFICATION_ISOSPECIFICATION` | [`QUALITYHEADER`](../QUALITY/QUALITYHEADER.md) | `COMPANYCODE`, `ISOSPECIFICATIONCODE` | `QUALITYHEADER.COMPANYCODE = ISOSPECIFICATION.COMPANYCODE AND QUALITYHEADER.ISOSPECIFICATIONCODE = ISOSPECIFICATION.CODE` |
| `ISOSPECIFICATION_ISOSPECIFICATION` | [`QUALITYLINE`](../QUALITY/QUALITYLINE.md) | `QUALITYHEADERCOMPANYCODE`, `ISOSPECIFICATIONCODE` | `QUALITYLINE.QUALITYHEADERCOMPANYCODE = ISOSPECIFICATION.COMPANYCODE AND QUALITYLINE.ISOSPECIFICATIONCODE = ISOSPECIFICATION.CODE` |
| `ISOSPECIFICATION_ISOSPECIFICATION` | [`QUALITYCERTIFICATEDETAIL`](../QUALITY/QUALITYCERTIFICATEDETAIL.md) | `QUALITYCERTCOMPANYCODE`, `ISOSPECIFICATIONCODE` | `QUALITYCERTIFICATEDETAIL.QUALITYCERTCOMPANYCODE = ISOSPECIFICATION.COMPANYCODE AND QUALITYCERTIFICATEDETAIL.ISOSPECIFICATIONCODE = ISOSPECIFICATION.CODE` |

## Indexes

- `ISOSPECIFICATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.ISOSPECIFICATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
