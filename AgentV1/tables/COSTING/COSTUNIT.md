# DB2ADMIN.COSTUNIT

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101055

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `RESPONSIBLEMANAGER` | CHAR(30) |  |  |  |  |
| 8 | `INITIALDATE` | DATE |  |  |  |  |
| 9 | `FINALDATE` | DATE |  |  |  |  |
| 10 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COSTUNIT.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTUNIT.COMPANYCODE = DIVISION.COMPANYCODE AND COSTUNIT.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COSTUNIT_COSTUNIT` | [`FINVOULINESCRIT`](../FINANCE/FINVOULINESCRIT.md) | `FINVOULINFINVOUHDRCOMPANYCODE`, `COSTUNITCODE` | `FINVOULINESCRIT.FINVOULINFINVOUHDRCOMPANYCODE = COSTUNIT.COMPANYCODE AND FINVOULINESCRIT.COSTUNITCODE = COSTUNIT.CODE` |
| `COSTUNIT_COSTUNIT` | [`GENERALLEDGERACCOUNT`](../FINANCE/GENERALLEDGERACCOUNT.md) | `COMPANYCODE`, `COSTUNITCODE` | `GENERALLEDGERACCOUNT.COMPANYCODE = COSTUNIT.COMPANYCODE AND GENERALLEDGERACCOUNT.COSTUNITCODE = COSTUNIT.CODE` |

## Indexes

- `COSTUNITUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.RESPONSIBLEMANAGER,
       t.INITIALDATE,
       t.FINALDATE,
       t.INACTIVE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.COSTUNIT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
