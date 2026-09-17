# DB2ADMIN.HSNGSTMAPPING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `MODULENAME`, `TARRIFCODE`, `IGSTTAXTEMPLATETEMPLATETYPE`, `IGSTTAXTEMPLATECODE`, `SGSTTAXTEMPLATETEMPLATETYPE`, `SGSTTAXTEMPLATECODE`, `INTERGSTTAXTMPTEMPLATETYPE`, `INTERGSTTAXTEMPLATECODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129021

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MODULENAME` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `TARRIFCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `IGSTTAXTEMPLATETEMPLATETYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `IGSTTAXTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `SGSTTAXTEMPLATETEMPLATETYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 6 | `SGSTTAXTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `INTERGSTTAXTMPTEMPLATETYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 8 | `INTERGSTTAXTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `EXPORTGSTTAXTMPTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 10 | `EXPORTGSTTAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `RCMIGSTTAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 12 | `RCMIGSTTAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 13 | `RCMSGSTTAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 14 | `RCMSGSTTAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 15 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 16 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `HSNGSTMAPPING.COMPANYCODE = COMPANY.CODE` |
| `TARIFF_TARRIF` | `TARRIFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `HSNGSTMAPPING.TARRIFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `HSNGSTMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MODULENAME,
       t.TARRIFCODE,
       t.IGSTTAXTEMPLATETEMPLATETYPE,
       t.IGSTTAXTEMPLATECODE,
       t.SGSTTAXTEMPLATETEMPLATETYPE,
       t.SGSTTAXTEMPLATECODE,
       t.INTERGSTTAXTMPTEMPLATETYPE,
       t.INTERGSTTAXTEMPLATECODE,
       t.EXPORTGSTTAXTMPTEMPLATETYPE,
       t.EXPORTGSTTAXTEMPLATECODE,
       t.RCMIGSTTAXTEMPLATETEMPLATETYPE
FROM   DB2ADMIN.HSNGSTMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
