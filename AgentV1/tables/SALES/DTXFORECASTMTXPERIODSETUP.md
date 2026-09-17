# DB2ADMIN.DTXFORECASTMTXPERIODSETUP

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204528

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `PERIODTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `NROFPERIODS` | INTEGER | NOT NULL |  |  |  |
| 7 | `ORDERTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `PLANNINGTEMPLATECODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `PLANPERIODIZEDCALENDARCODE` | CHAR(10) |  | FK | foreign_key |  |
| 10 | `SHIFTORDERDATE` | CHAR(1) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUP.COMPANYCODE = COMPANY.CODE` |
| `PERIODIZEDCALENDARTYPE_PERIODTYPE` | `PERIODTYPECODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUP.PERIODTYPECODE = PERIODIZEDCALENDARTYPE.CODE` |
| `PERIODIZEDCALENDARTYPE_PLANPERIODIZEDCALENDAR` | `PLANPERIODIZEDCALENDARCODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUP.PLANPERIODIZEDCALENDARCODE = PERIODIZEDCALENDARTYPE.CODE` |
| `PLANNINGTEMPLATE_PLANNINGTEMPLATE` | `COMPANYCODE`, `PLANNINGTEMPLATECODE` | [`PLANNINGTEMPLATE`](../SALES/PLANNINGTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUP.COMPANYCODE = PLANNINGTEMPLATE.COMPANYCODE AND DTXFORECASTMTXPERIODSETUP.PLANNINGTEMPLATECODE = PLANNINGTEMPLATE.CODE` |
| `SALESORDERTEMPLATE_ORDERTEMPLATE` | `COMPANYCODE`, `ORDERTEMPLATECODE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUP.COMPANYCODE = SALESORDERTEMPLATE.COMPANYCODE AND DTXFORECASTMTXPERIODSETUP.ORDERTEMPLATECODE = SALESORDERTEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DTXFORECASTMTXPERIODSETUP_DETAIL` | [`DTXFORECASTMTXPERIODSETUPDTL`](../WAREHOUSE/DTXFORECASTMTXPERIODSETUPDTL.md) | `FORECASTMTXSETUPCOMPANYCODE`, `FORECASTMTXSETUPCODE` | `DTXFORECASTMTXPERIODSETUPDTL.FORECASTMTXSETUPCOMPANYCODE = DTXFORECASTMTXPERIODSETUP.COMPANYCODE AND DTXFORECASTMTXPERIODSETUPDTL.FORECASTMTXSETUPCODE = DTXFORECASTMTXPERIODSETUP.CODE` |

## Indexes

- `DTXFORECASTMTXPERIODSETUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PERIODTYPECODE,
       t.NROFPERIODS,
       t.ORDERTEMPLATECODE,
       t.PLANNINGTEMPLATECODE,
       t.PLANPERIODIZEDCALENDARCODE,
       t.SHIFTORDERDATE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.DTXFORECASTMTXPERIODSETUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
