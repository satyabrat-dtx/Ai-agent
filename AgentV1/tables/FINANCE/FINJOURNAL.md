# DB2ADMIN.FINJOURNAL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101627

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `INITIALDATE` | DATE |  |  |  |  |
| 8 | `FINALDATE` | DATE |  |  |  |  |
| 9 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINJOURNAL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINJOURNAL.COMPANYCODE = DIVISION.COMPANYCODE AND FINJOURNAL.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINJOURNAL_JOURNAL` | [`FINVOUHEADER`](../FINANCE/FINVOUHEADER.md) | `COMPANYCODE`, `JOURNALCODE` | `FINVOUHEADER.COMPANYCODE = FINJOURNAL.COMPANYCODE AND FINVOUHEADER.JOURNALCODE = FINJOURNAL.CODE` |
| `FINJOURNAL_JOURNAL` | [`FINVOUCHERTEMPLATE`](../FINANCE/FINVOUCHERTEMPLATE.md) | `COMPANYCODE`, `JOURNALCODE` | `FINVOUCHERTEMPLATE.COMPANYCODE = FINJOURNAL.COMPANYCODE AND FINVOUCHERTEMPLATE.JOURNALCODE = FINJOURNAL.CODE` |
| `FINJOURNAL_JOURNAL` | [`FINANCIALCUSTOMIZEDOPTIONS`](../FINANCE/FINANCIALCUSTOMIZEDOPTIONS.md) | `COMPANYCODE`, `JOURNALCODE` | `FINANCIALCUSTOMIZEDOPTIONS.COMPANYCODE = FINJOURNAL.COMPANYCODE AND FINANCIALCUSTOMIZEDOPTIONS.JOURNALCODE = FINJOURNAL.CODE` |

## Indexes

- `FINJOURNALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.INITIALDATE,
       t.FINALDATE,
       t.INACTIVE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINJOURNAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
