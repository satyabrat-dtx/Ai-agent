# DB2ADMIN.QUALITYCERTIFICATETEMPLATE

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192942

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `COMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 6 | `COMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 7 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYCERTIFICATETEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `QACERTIFICATECOMMENTSCKHEADER_COMMENTCHOOSEKEYS` | `COMPANYCODE`, `COMMENTCHOOSEKEYSCODE` | [`QACERTIFICATECOMMENTSCKHEADER`](../QUALITY/QACERTIFICATECOMMENTSCKHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCERTIFICATETEMPLATE.COMPANYCODE = QACERTIFICATECOMMENTSCKHEADER.COMPANYCODE AND QUALITYCERTIFICATETEMPLATE.COMMENTCHOOSEKEYSCODE = QACERTIFICATECOMMENTSCKHEADER.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QUALITYCERTIFICATETEMPLATE_QUALITYCERTIFICATETEMPLATE` | [`QUALITYCERTIFICATE`](../QUALITY/QUALITYCERTIFICATE.md) | `COMPANYCODE`, `QUALITYCERTIFICATETEMPLATECODE` | `QUALITYCERTIFICATE.COMPANYCODE = QUALITYCERTIFICATETEMPLATE.COMPANYCODE AND QUALITYCERTIFICATE.QUALITYCERTIFICATETEMPLATECODE = QUALITYCERTIFICATETEMPLATE.CODE` |
| `QUALITYCERTIFICATETEMPLATE_QUALITYCERTIFICATETEMPLATE` | [`QACERTIFICATECMTDEFINITION`](../QUALITY/QACERTIFICATECMTDEFINITION.md) | `COMPANYCODE`, `QUALITYCERTIFICATETEMPLATECODE` | `QACERTIFICATECMTDEFINITION.COMPANYCODE = QUALITYCERTIFICATETEMPLATE.COMPANYCODE AND QACERTIFICATECMTDEFINITION.QUALITYCERTIFICATETEMPLATECODE = QUALITYCERTIFICATETEMPLATE.CODE` |

## Indexes

- `QUALITYCERTIFICATETEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COMMENTCRITERIA,
       t.COMMENTPOLICYCODE,
       t.COMMENTCHOOSEKEYSCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.QUALITYCERTIFICATETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
