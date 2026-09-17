# DB2ADMIN.PERIODMASTER

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `MODUL`, `INFOTYPECODE`, `FISCALYEAR`, `ABBREVFISCALYEAR`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103015

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `MODUL` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `INFOTYPECODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FISCALYEAR` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 5 | `ABBREVFISCALYEAR` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 6 | `PERIODDEFINITION` | INTEGER | NOT NULL |  |  |  |
| 7 | `INITIALDATE` | DATE |  |  |  |  |
| 8 | `FINALDATE` | DATE |  |  |  |  |
| 9 | `TOTALPERIODS` | INTEGER | NOT NULL |  |  |  |
| 10 | `SPECIALPERIOD` | INTEGER | NOT NULL |  |  |  |
| 11 | `CALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 12 | `FIRSTQUARTER` | DATE |  |  |  |  |
| 13 | `SECONDQUARTER` | DATE |  |  |  |  |
| 14 | `THIRDQUARTER` | DATE |  |  |  |  |
| 15 | `DIVIDER` | INTEGER | NOT NULL |  |  |  |
| 16 | `OPENINGBALANCE` | TIMESTAMP |  |  |  |  |
| 17 | `OPENINGUSER` | CHAR(25) |  |  |  |  |
| 18 | `YEARENDCLOSE` | SMALLINT | NOT NULL |  |  |  |
| 19 | `YEARENDCLOSEINFO` | TIMESTAMP |  |  |  |  |
| 20 | `YEARENDCLOSEUSER` | CHAR(25) |  |  |  |  |
| 21 | `CLOSINGDATECPA` | DATE |  |  |  |  |
| 22 | `CLOSINGAUDITOR` | CHAR(30) |  |  |  |  |
| 23 | `ARCHIVED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `ARCHIVEDDATE` | TIMESTAMP |  |  |  |  |
| 25 | `ARCHIVEDUSER` | CHAR(25) |  |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PERIODMASTER.COMPANYCODE = COMPANY.CODE` |
| `FININFOTYPE_INFOTYPE` | `INFOTYPECODE` | [`FININFOTYPE`](../FINANCE/FININFOTYPE.md) | `CODE` | RESTRICT | `PERIODMASTER.INFOTYPECODE = FININFOTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PERIODMASTER_PERIODS` | [`PERIODMASTERCHILD`](../FINANCE/PERIODMASTERCHILD.md) | `PERIODMASTERCOMPANYCODE`, `PERIODMASTERDIVISIONCODE`, `PERIODMASTERMODUL`, `PERIODMASTERINFOTYPECODE`, `PERIODMASTERFISCALYEAR`, `PERIODMASTERABBREVFISCALYEAR` | `PERIODMASTERCHILD.PERIODMASTERCOMPANYCODE = PERIODMASTER.COMPANYCODE AND PERIODMASTERCHILD.PERIODMASTERDIVISIONCODE = PERIODMASTER.DIVISIONCODE AND PERIODMASTERCHILD.PERIODMASTERMODUL = PERIODMASTER.MODUL AND PERIODMASTERCHILD.PERIODMASTERINFOTYPECODE = PERIODMASTER.INFOTYPECODE AND PERIODMASTERCHILD.PERIODMASTERFISCALYEAR = PERIODMASTER.FISCALYEAR AND PERIODMASTERCHILD.PERIODMASTERABBREVFISCALYEAR = PERIODMASTER.ABBREVFISCALYEAR` |

## Indexes

- `PERIODMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.MODUL,
       t.INFOTYPECODE,
       t.FISCALYEAR,
       t.ABBREVFISCALYEAR,
       t.PERIODDEFINITION,
       t.INITIALDATE,
       t.FINALDATE,
       t.TOTALPERIODS,
       t.SPECIALPERIOD,
       t.CALCULATION
FROM   DB2ADMIN.PERIODMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
