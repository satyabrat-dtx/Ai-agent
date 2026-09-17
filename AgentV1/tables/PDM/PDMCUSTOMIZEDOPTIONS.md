# DB2ADMIN.PDMCUSTOMIZEDOPTIONS

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 1 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 75841

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SUBCODEPOLICYREFERENCECODE` | CHAR(20) |  |  |  |  |
| 2 | `PDM2QUALITYBARCODETYPE` | CHAR(10) |  |  |  |  |
| 3 | `BARCODEADENTITYNAME` | CHAR(50) |  | FK | foreign_key |  |
| 4 | `BARCODEADNAME` | CHAR(50) |  | FK | foreign_key |  |
| 5 | `LANGUAGEFORERRORSCODE` | CHAR(2) |  | FK | foreign_key |  |
| 6 | `EXPORTENVIRONMENTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 7 | `EXISTSRTGPOLICYREFERENCECODE` | CHAR(20) |  |  |  |  |
| 8 | `GENERICSIZETYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `GENERICSIZETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `TECHDATATOFIKD` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `COLORHANDLING` | CHAR(1) |  |  |  |  |
| 13 | `EXPORTQADOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `BOMCMPMULTIPLERULE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_BARCODEAD` | `BARCODEADENTITYNAME`, `BARCODEADNAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `PDMCUSTOMIZEDOPTIONS.BARCODEADENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND PDMCUSTOMIZEDOPTIONS.BARCODEADNAME = ADADDITIONALDATA.NAME` |
| `EXPORTENVIRONMENT_EXPORTENVIRONMENT` | `EXPORTENVIRONMENTCODE` | [`EXPORTENVIRONMENT`](../PDM/EXPORTENVIRONMENT.md) | `CODE` | RESTRICT | `PDMCUSTOMIZEDOPTIONS.EXPORTENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |
| `LANGUAGES_LANGUAGEFORERRORS` | `LANGUAGEFORERRORSCODE` | [`LANGUAGES`](../PLATFORM/LANGUAGES.md) | `CODE` | RESTRICT | `PDMCUSTOMIZEDOPTIONS.LANGUAGEFORERRORSCODE = LANGUAGES.CODE` |
| `SIZESTYPE_GENERICSIZETYPE` | `GENERICSIZETYPECOMPANYCODE`, `GENERICSIZETYPECODE` | [`SIZESTYPE`](../PDM/SIZESTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PDMCUSTOMIZEDOPTIONS.GENERICSIZETYPECOMPANYCODE = SIZESTYPE.COMPANYCODE AND PDMCUSTOMIZEDOPTIONS.GENERICSIZETYPECODE = SIZESTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PDMCUSTOMIZEDOPTIONS_PDMCFG` | [`PDMCONFIGURATION`](../PDM/PDMCONFIGURATION.md) | `PDMCUSTOMIZEDOPTIONSCMYCODE` | `PDMCONFIGURATION.PDMCUSTOMIZEDOPTIONSCMYCODE = PDMCUSTOMIZEDOPTIONS.COMPANYCODE` |

## Indexes

- `PDMCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SUBCODEPOLICYREFERENCECODE,
       t.PDM2QUALITYBARCODETYPE,
       t.BARCODEADENTITYNAME,
       t.BARCODEADNAME,
       t.LANGUAGEFORERRORSCODE,
       t.EXPORTENVIRONMENTCODE,
       t.EXISTSRTGPOLICYREFERENCECODE,
       t.GENERICSIZETYPECOMPANYCODE,
       t.GENERICSIZETYPECODE,
       t.TECHDATATOFIKD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PDMCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
