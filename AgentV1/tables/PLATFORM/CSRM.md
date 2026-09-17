# DB2ADMIN.CSRM

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 2 of 2 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 10 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118364

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 8 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `ORDERPARTNERTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 11 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `LETTERTEMPLATECODE` | CHAR(30) |  | FK | foreign_key |  |
| 13 | `PROPOSALDATE` | DATE | NOT NULL |  |  |  |
| 14 | `PLANNEDSTARTDATE` | DATE |  |  |  |  |
| 15 | `PLANNEDENDDATE` | DATE |  |  |  |  |
| 16 | `OWNERUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 17 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 18 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 19 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 20 | `PROJECTDATE` | DATE |  |  |  |  |
| 21 | `BRIEF` | VARCHAR(1000) | NOT NULL |  |  |  |
| 22 | `ACTUALSTARTDATE` | DATE |  |  |  |  |
| 23 | `ACTUALENDDATE` | DATE |  |  |  |  |
| 24 | `CLOSINGCOMMENT` | VARCHAR(1000) |  |  |  |  |
| 25 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 10

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLETTERTEMPLATE_LETTERTEMPLATE` | `COMPANYCODE`, `LETTERTEMPLATECODE` | [`ABSLETTERTEMPLATE`](../PLATFORM/ABSLETTERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRM.COMPANYCODE = ABSLETTERTEMPLATE.COMPANYCODE AND CSRM.LETTERTEMPLATECODE = ABSLETTERTEMPLATE.CODE` |
| `ABSUSERDEF_OWNER` | `OWNERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `CSRM.OWNERUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CSRM.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRM.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND CSRM.COUNTERCODE = COUNTER.CODE` |
| `CSRMTEMPLATE_TEMPLATE` | `COMPANYCODE`, `TEMPLATECODE` | [`CSRMTEMPLATE`](../PLATFORM/CSRMTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRM.COMPANYCODE = CSRMTEMPLATE.COMPANYCODE AND CSRM.TEMPLATECODE = CSRMTEMPLATE.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRM.COMPANYCODE = DEPARTMENT.COMPANYCODE AND CSRM.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRM.COMPANYCODE = DIVISION.COMPANYCODE AND CSRM.DIVISIONCODE = DIVISION.CODE` |
| `ORDERPARTNER_CUSTOMER` | `COMPANYCODE`, `CUSTOMERCUSTOMERSUPPLIERTYPE`, `CUSTOMERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `CSRM.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND CSRM.CUSTOMERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND CSRM.CUSTOMERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `ORDERPARTNER_SUPPLIER` | `COMPANYCODE`, `SUPPLIERCUSTOMERSUPPLIERTYPE`, `SUPPLIERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `CSRM.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND CSRM.SUPPLIERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND CSRM.SUPPLIERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRM.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND CSRM.PLANTCODE = PLANT.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CSRM_CSRMPARTICIPANT` | [`CSRMPARTICIPANT`](../PLATFORM/CSRMPARTICIPANT.md) | `CSRMCOMPANYCODE`, `CSRMCOUNTERCODE`, `CSRMCODE` | `CSRMPARTICIPANT.CSRMCOMPANYCODE = CSRM.COMPANYCODE AND CSRMPARTICIPANT.CSRMCOUNTERCODE = CSRM.COUNTERCODE AND CSRMPARTICIPANT.CSRMCODE = CSRM.CODE` |

## Indexes

- `CSRMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.DEPARTMENTCODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.ORDERPARTNERTYPE,
       t.SUPPLIERCUSTOMERSUPPLIERTYPE,
       t.SUPPLIERCUSTOMERSUPPLIERCODE
FROM   DB2ADMIN.CSRM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
