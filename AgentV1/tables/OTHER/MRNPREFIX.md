# DB2ADMIN.MRNPREFIX

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 133691

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 7 | `TERMSOFLOGCODE` | CHAR(2) |  | FK | foreign_key |  |
| 8 | `USEDFORJOBWORK` | SMALLINT | NOT NULL |  |  |  |
| 9 | `AUTOLOTNUMBERFLAG` | SMALLINT | NOT NULL |  |  |  |
| 10 | `LOTLENGTH` | INTEGER | NOT NULL |  |  |  |
| 11 | `SERVICEBILLFLAG` | SMALLINT | NOT NULL |  |  |  |
| 12 | `EXCHANGERATEON` | CHAR(3) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `MRNPOSTINGBY` | CHAR(1) |  |  |  |  |
| 21 | `QUALITYCHECKREQUIRED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MRNPREFIX.COMPANYCODE = COMPANY.CODE` |
| `NETTOLOG_TERMSOFLOG` | `COMPANYCODE`, `TERMSOFLOGCODE` | [`NETTOLOG`](../LOCALIZATION/NETTOLOG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MRNPREFIX.COMPANYCODE = NETTOLOG.COMPANYCODE AND MRNPREFIX.TERMSOFLOGCODE = NETTOLOG.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MRNPREFIX_MRNPREFIX` | [`PURCHASEORDERTEMPLATEIE`](../PURCHASING/PURCHASEORDERTEMPLATEIE.md) | `COMPANYCODE`, `MRNPREFIXDIVISIONCODE`, `MRNPREFIXCODE` | `PURCHASEORDERTEMPLATEIE.COMPANYCODE = MRNPREFIX.COMPANYCODE AND PURCHASEORDERTEMPLATEIE.MRNPREFIXDIVISIONCODE = MRNPREFIX.DIVISIONCODE AND PURCHASEORDERTEMPLATEIE.MRNPREFIXCODE = MRNPREFIX.CODE` |
| `MRNPREFIX_MRNPREFIX` | [`MRNCREATIONCONTROL`](../OTHER/MRNCREATIONCONTROL.md) | `COMPANYCODE`, `DIVISIONCODE`, `MRNPREFIXCODE` | `MRNCREATIONCONTROL.COMPANYCODE = MRNPREFIX.COMPANYCODE AND MRNCREATIONCONTROL.DIVISIONCODE = MRNPREFIX.DIVISIONCODE AND MRNCREATIONCONTROL.MRNPREFIXCODE = MRNPREFIX.CODE` |
| `MRNPREFIX_MRNPREFIX` | [`MRNHEADER`](../CORE_MASTER/MRNHEADER.md) | `COMPANYCODE`, `DIVISIONCODE`, `MRNPREFIXCODE` | `MRNHEADER.COMPANYCODE = MRNPREFIX.COMPANYCODE AND MRNHEADER.DIVISIONCODE = MRNPREFIX.DIVISIONCODE AND MRNHEADER.MRNPREFIXCODE = MRNPREFIX.CODE` |

## Indexes

- `MRNPREFIXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.LOGMANAGEMENT,
       t.TERMSOFLOGCODE,
       t.USEDFORJOBWORK,
       t.AUTOLOTNUMBERFLAG,
       t.LOTLENGTH,
       t.SERVICEBILLFLAG
FROM   DB2ADMIN.MRNPREFIX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
